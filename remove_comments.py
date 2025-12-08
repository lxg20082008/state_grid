#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
删除Python文件中所有#注释的脚本
支持删除整行注释和行尾注释
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path

def remove_python_comments(content):
    """
    删除Python代码中的注释
    会正确处理字符串中的#字符，避免误删
    """
    lines = content.splitlines()
    result_lines = []
    
    # 用于跟踪是否在多行字符串中
    in_multiline_string = False
    string_delimiter = None
    
    for line in lines:
        # 处理多行字符串的开始/结束
        if not in_multiline_string:
            # 检查是否开始多行字符串
            triple_quotes = re.findall(r'(\"\"\"|\'\'\')', line)
            if triple_quotes:
                # 简单处理：如果找到三引号，标记为在多行字符串中
                # 实际应该更复杂，需要处理成对的引号
                in_multiline_string = True
                string_delimiter = triple_quotes[0]
                # 如果三引号在同一行结束
                if line.count(string_delimiter) >= 2:
                    in_multiline_string = False
                result_lines.append(line)
                continue
        
        if in_multiline_string:
            # 在多行字符串中，保留所有内容
            result_lines.append(line)
            # 检查是否结束多行字符串
            if string_delimiter in line:
                # 简单检查：如果包含结束引号，结束多行字符串
                # 注意：这并不完全准确
                in_multiline_string = False
            continue
        
        # 不在多行字符串中，处理注释
        processed_line = ''
        in_string = False
        string_char = ''
        i = 0
        
        while i < len(line):
            char = line[i]
            
            # 处理转义字符
            if in_string and char == '\\':
                processed_line += char
                i += 1
                if i < len(line):
                    processed_line += line[i]
                i += 1
                continue
            
            # 处理字符串开始/结束
            if not in_string and (char == '"' or char == "'"):
                # 检查是否是三引号
                if i + 2 < len(line) and line[i:i+3] == char*3:
                    # 开始或结束多行字符串
                    processed_line += line[i:i+3]
                    i += 3
                    continue
                else:
                    # 单引号字符串
                    in_string = True
                    string_char = char
                    processed_line += char
                    i += 1
                    continue
            elif in_string and char == string_char:
                in_string = False
                processed_line += char
                i += 1
                continue
            
            # 如果不在字符串中，遇到#则删除从#开始到行尾的内容
            if not in_string and char == '#':
                break  # 停止处理该行的剩余部分
            
            processed_line += char
            i += 1
        
        # 去除行尾空白
        processed_line = processed_line.rstrip()
        
        # 如果处理后的行不为空，添加到结果
        if processed_line:
            result_lines.append(processed_line)
    
    return '\n'.join(result_lines)

def process_file(filepath, backup=True, dry_run=False):
    """处理单个文件"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        new_content = remove_python_comments(content)
        
        # 检查是否有变化
        if original_content != new_content:
            lines_removed = original_content.count('\n') - new_content.count('\n')
            
            if dry_run:
                print(f"[DRY RUN] 将修改: {filepath} (删除约 {lines_removed} 行)")
                return True, lines_removed
            
            # 备份原文件
            if backup:
                backup_path = filepath + '.bak'
                shutil.copy2(filepath, backup_path)
                print(f"已备份原文件到: {backup_path}")
            
            # 写入新内容
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"已处理: {filepath} (删除了 {lines_removed} 行注释)")
            return True, lines_removed
        else:
            if not dry_run:
                print(f"无变化: {filepath}")
            return False, 0
    
    except Exception as e:
        print(f"处理文件 {filepath} 时出错: {e}")
        return False, 0

def process_directory(directory='.', extensions=('.py',), 
                     backup=True, dry_run=False, recursive=True):
    """处理目录下的所有文件"""
    processed_count = 0
    total_lines_removed = 0
    skipped_files = 0
    
    directory = Path(directory)
    
    if recursive:
        file_generator = directory.rglob('*.py')
    else:
        file_generator = directory.glob('*.py')
    
    for filepath in file_generator:
        if filepath.suffix.lower() in extensions:
            if filepath.name.endswith('.bak'):
                continue  # 跳过备份文件
            
            processed, lines_removed = process_file(filepath, backup, dry_run)
            if processed:
                processed_count += 1
                total_lines_removed += lines_removed
            else:
                skipped_files += 1
        else:
            skipped_files += 1
    
    return processed_count, total_lines_removed, skipped_files

def main():
    parser = argparse.ArgumentParser(
        description='删除Python文件中的#注释',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s                    # 处理当前目录及子目录的所有.py文件
  %(prog)s -d /path/to/code   # 处理指定目录
  %(prog)s --no-backup        # 不创建备份文件
  %(prog)s --dry-run          # 模拟运行，不实际修改文件
  %(prog)s --no-recursive     # 仅处理当前目录，不处理子目录
        """
    )
    
    parser.add_argument('-d', '--directory', default='.',
                       help='要处理的目录 (默认: 当前目录)')
    parser.add_argument('--no-backup', action='store_true',
                       help='不创建备份文件 (默认会创建.bak备份)')
    parser.add_argument('--dry-run', action='store_true',
                       help='模拟运行，显示将进行的更改但不实际修改文件')
    parser.add_argument('--no-recursive', action='store_true',
                       help='仅处理指定目录，不递归处理子目录')
    parser.add_argument('--extensions', default='.py',
                       help='要处理的文件扩展名，用逗号分隔 (默认: .py)')
    
    args = parser.parse_args()
    
    # 解析扩展名
    extensions = tuple(ext.strip() for ext in args.extensions.split(','))
    
    print("Python注释删除工具")
    print("=" * 50)
    
    if args.dry_run:
        print("模拟运行模式: 不会实际修改文件")
    
    if args.no_backup and not args.dry_run:
        print("警告: 未启用备份，原文件将被直接修改!")
        confirm = input("确定继续吗? (y/N): ")
        if confirm.lower() != 'y':
            print("操作已取消")
            return
    
    backup = not args.no_backup
    recursive = not args.no_recursive
    
    try:
        processed_count, total_lines_removed, skipped_files = process_directory(
            args.directory, extensions, backup, args.dry_run, recursive
        )
        
        print("\n" + "=" * 50)
        print("处理完成!")
        print(f"处理文件数: {processed_count}")
        print(f"跳过文件数: {skipped_files}")
        print(f"删除注释行数: {total_lines_removed}")
        
        if backup and processed_count > 0 and not args.dry_run:
            print(f"\n备份文件已创建，扩展名为 .bak")
            print("如需恢复原文件，请手动删除修改后的文件，并将.bak文件重命名去除.bak后缀")
    
    except KeyboardInterrupt:
        print("\n\n操作被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n发生错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()