_Au='daily_ele'
_At='month_meter_num'
_As='constType'
_Ar='queryYear'
_Aq='provinceCode'
_Ap='redirect_url'
_Ao='refresh_interval'
_An='dataVersion'
_Am='doorAccountDict'
_Al='refreshToken'
_Ak='accessToken'
_Aj='brightness'
_Ai='BCP_00026'
_Ah='serviceCode_smt'
_Ag='WEBA10070900'
_Af='serviceType'
_Ae='jM_custType'
_Ad='jM_busiTypeCode'
_Ac='doorNumberManeger'
_Ab='proCode'
_Aa='loginAccount'
_AZ='userAccountId'
_AY='elecTypeCode'
_AX='quInfo'
_AW='blockY'
_AV='blockSrc'
_AU='canvasSrc'
_AT='powerUserList'
_AS='userInfo'
_AR='publicKey'
_AQ='WEBA10070800'
_AP='timeDay'
_AO='WEBA10070700'
_AN='state_grid'
_AM='channelNo'
_AL='month_ele'
_AK='consType'
_AJ='provinceId'
_AI='userName'
_AH='acctId'
_AG='bizrt'
_AF='password'
_AE='0101046'
_AD='month_ele_num'
_AC='consNo'
_AB='list'
_AA='token'
_A9='keyCode'
_A8='querytypeCode'
_A7='01010049'
_A6='month_t_ele_num'
_A5='month_n_ele_num'
_A4='month_v_ele_num'
_A3='month_p_ele_num'
_A2='thisTPq'
_A1='thisNPq'
_A0='thisVPq'
_z='thisPPq'
_y='errmsg'
_x='BCP_000026'
_w='app'
_v='WEBALIPAY_01'
_u='order'
_t='dayElePq'
_s='timestamp'
_r='authFlag'
_q='09'
_p='0101183'
_o='tenant'
_n='devciceId'
_m='devciceIp'
_l='member'
_k='stepelect'
_j='account'
_i='daily_bill_list'
_h='orgNo'
_g='consNo_dst'
_f='srvrt'
_e='0101154'
_d='getday'
_c='clearCache'
_b='promotCode'
_a='01'
_Z='month'
_Y='account_balance'
_X='proNo'
_W='userId'
_V=True
_U='SGAPP'
_T='target'
_S='month_bill_list'
_R='promotType'
_Q='uscInfo'
_P='subBusiTypeCode'
_O='serialNo'
_N=False
_M='0902'
_L='srvCode'
_K='serCat'
_J='busiTypeCode'
_I='code'
_H='channelCode'
_G='errcode'
_F='1'
_E='source'
_D=None
_C='serviceCode'
_B='funcCode'
_A='data'
import json,time,urllib.parse,datetime
from.const import VERSION
from.utils.logger import LOGGER
from.utils.store import async_save_to_store
from.utils.crypt import a,b,c,d,e
import hashlib
import io,base64
from PIL import Image
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.components import persistent_notification
MAX_RETRIES=3
configuration={_Q:{_l:_M,_m:'',_n:'',_o:_AN},_E:_U,_T:'32101',_H:_M,_AM:_M,'toPublish':_a,'siteId':'2012000000033700',_L:'',_O:'',_B:'',_C:{_u:_e,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343','submit':'0101003','sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',_E:_M},'subscriptionList':{_L:'APP_SGPMS_05_030',_O:'22',_H:_M,_B:'22',_T:'-1'},'userInformation':{_C:'01008183',_E:_U},'userInform':{_C:_p,_E:_U},'elesum':{_H:_M,_B:_v,_b:_F,_R:_F,_C:'0101143',_E:_w},_j:{_H:_M,_B:'WEBA1007200'},_Ac:{_E:_M,_T:'-1',_H:_q,_AM:_q,_C:_A7,_B:'WEBA40050000',_Q:{_l:_M,_m:'',_n:'',_o:_AN}},'doorAuth':{_E:_U,_C:'f04'},'xinZ':{_K:'101',_Ad:'101','fJ_busiTypeCode':'102',_Ae:'03','fJ_custType':'02',_Af:_a,_P:'',_B:_AO,_u:_e,_E:_U,_A8:_F},'onedo':{_C:_AE,_E:_U,_B:_AO,'queryType':'03'},'xinHuTongDian':{_K:'110',_J:'211',_P:'21102',_B:'WEBA10071200',_H:_M,_E:_q,_C:_p},'company':{_K:'104',_B:_AO,_Af:'02',_A8:_F,_r:_F,_E:_U,_u:_e},'charge':{_H:_q,_B:'WEBA10071300',_AM:'0901',_K:'102',_Ae:_a,_Ad:'102'},'other':{_H:_q,_B:'WEBA10079700',_K:'129',_J:'999',_P:'21501',_C:_x,_L:'',_O:''},'vatchange':{'submit':'0101003',_J:'320',_P:'',_K:'115',_B:'WEBA10074000',_r:_F},'bill':{_c:_F,_B:_v,_R:_F,_C:_x},_k:{_H:_M,_B:_v,_R:_F,_c:_q,_C:_x,_E:_w},_d:{_H:_M,_c:'11',_B:_v,_b:_F,_R:_F,_C:_x,_E:_w},'mouthOut':{_H:_M,_c:'11',_B:_v,_b:_F,_R:_F,_C:_x,_E:_w},'meter':{_K:'114',_J:'304',_B:'WEBA10071000',_P:'',_C:_AE,_O:''},'complaint':{_J:'005','srvMode':_M,'anonymousFlag':'0','replyMode':_a,'retvisitFlag':_a},'report':{_J:'006'},'tradewinds':{_J:'019'},'somesay':{_J:'091'},'faultrepair':{_B:_Ag,_C:_p,_K:'111',_J:'001',_P:'21505'},'electronicInvoice':{_K:'105',_J:'0'},'rename':{_C:_AE,_B:'WEBA10076100',_J:'210',_K:'109',_r:_F,'gh_busiTypeCode':'211','gh_subusi':'21101',_O:'',_L:''},'pause':{_P:'',_C:_A7,_B:'WEBA10073600',_K:'107',_J:'203','jr_busi':'201',_O:'',_L:''},'capacityRecovery':{_C:_A7,_E:_U,_L:'',_O:'',_B:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',_J:'202',_P:'',_K:'108',_AP:'5',_r:_F},'electricityPriceChange':{_C:_p,_J:'215',_P:'21502',_K:'113',_r:_F,_AP:'15',_B:'WEBA10073900WEB',_L:'',_O:''},'electricityPriceStrategyChange':{_C:'01008183',_J:'215',_P:'21506',_K:'160',_B:'WEBV00000517WEB',_L:'',_O:''},'eemandValueAdjustment':{_C:_p,_L:'',_O:'',_K:'112',_B:'WEBA10073800',_J:'215',_P:'21504',_r:_F,_AP:'5','getMonthServiceCode':_AE},'businessProgress':{_C:_p,_L:_a,_B:'WEB01'},'increase':{_E:_U,_O:'',_L:'',_Ah:_A7,_C:_e,_u:_e,_B:_AQ,_A8:_F,_K:'106',_J:'111',_P:''},'fjincrea':{_K:'105',_J:'110',_P:'',_E:_U,_B:_AQ,_O:'',_L:'',_Ah:_A7,_C:_e,_u:_e,_A8:_F},'persIncrea':{_K:'105',_J:'109',_u:_e,_P:'',_E:_U,_B:_AQ,_A8:_F},'fgdChange':{_C:_p,_L:_a,_H:_q,_B:_Ag,_J:'215',_P:'21505',_K:'111',_r:_F},'createOrder':{_H:_M,_B:_v,_L:'BCP_000001','chargeMode':'02','conType':_a,'bizTypeId':'BT_ELEC'},'largePopulation':{_J:'383',_B:'WEBA10076800',_P:'',_L:'',_R:'',_b:'',_H:'0901',_K:'383',_C:'',_O:''},'biaoJiCode':{_C:'0104507',_E:'1704',_H:'1704'},'twoGuar':{_J:'402',_P:'40201',_B:'web_twoGuar'},'electTrend':{_C:_Ai,_H:_M},'emergency':{_C:_Ai,_B:'A10000000',_H:_M},'infoPublic':{_C:'2545454',_E:_w}}
appKey='7e5b5e84ddad4994b0ebc68dedca4962'
appSecret='2bc37a881e1541aaa6e6e174658d150b'
baseApi='https://www.95598.cn/api'
get_request_key_api='/oauth2/outer/c02/f02'
get_request_authorize_api='/oauth2/oauth/authorize'
get_web_token_api='/oauth2/outer/getWebToken'
get_verify_code_api='/osg-web0004/open/c44/f05'
verify_password_api='/osg-web0004/open/c44/f06'
get_door_number_api='/osg-open-uc0001/member/c9/f02'
get_door_balance_api='/osg-open-bc0001/member/c05/f01'
get_door_bill_api='/osg-open-bc0001/member/c01/f02'
get_door_ladder_api='/osg-open-bc0001/member/c04/f03'
get_door_daily_bill_api='/osg-web0004/member/c24/f01'
sessionIdControlApiList=[verify_password_api,get_verify_code_api]
keyCodeControlApiList=[verify_password_api,get_verify_code_api,get_request_authorize_api,get_web_token_api,get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,get_door_daily_bill_api]
authControlApiList=[get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,get_door_daily_bill_api]
tControlApiList=[get_door_number_api,get_door_balance_api,get_door_bill_api,get_door_ladder_api,get_door_daily_bill_api]
def json_dumps(data):return json.dumps(data,separators=(',',':'),ensure_ascii=_N)
def normal_round(num,ndigits=0):
	A=ndigits
	if A==0:return int(num+.5)
	else:B=10**A;return int(num*B+.5)/B
def catchFloat(data,key):
	if key in data:
		try:return normal_round(float(data[key]),2)
		except:return 0
	else:return 0
def catchInt(data,key):
	if key in data:
		try:return normal_round(float(data[key]),0)
		except:return 0
	else:return 0
def get_month_date_range(date_str):
	C=date_str;A=int(C[:4]);B=int(C[4:]);F=datetime.date(A,B,1)
	if B==12:D=1;E=A+1
	else:D=B+1;E=A
	G=datetime.date(E,D,1)-datetime.timedelta(days=1);return A,F,G
def base64_image_to_bytes(base64_data):
	A=base64_data
	if A.startswith('data:image'):
		B=A.find(',')
		if B!=-1:A=A[B+1:]
	C=base64.b64decode(A);return C
def is_dark(pixel,threshold=100,method=_Aj):
	F=pixel;D=method
	if len(F)==4:
		A,B,C,G=F
		if G<128:return _N
	else:A,B,C=F
	if D==_Aj:H=max(A,B,C);I=min(A,B,C);E=H
	elif D=='average':E=(A+B+C)//3
	elif D=='max':E=max(A,B,C)
	elif D=='perceived':E=int(.299*A+.587*B+.114*C)
	else:raise ValueError(f"未知方法: {D}")
	return E<threshold
def find_max_rectangle(matrix):
	C=matrix
	if not C or not C[0]:return 0,0,0,0
	L,E=len(C),len(C[0]);D=[0]*E;G=0;H=0,0,0,0
	for F in range(L):
		for A in range(E):
			if C[F][A]==1:D[A]+=1
			else:D[A]=0
		B=[]
		for A in range(E+1):
			M=D[A]if A<E else-1
			while B and M<D[B[-1]]:
				N=B.pop();I=D[N];J=A if not B else A-B[-1]-1;K=I*J
				if K>G:G=K;O=F-I+1;P=A-J;Q=F;R=A-1;H=O,P,Q,R
			B.append(A)
	return H
class StateGridDataClient:
	hass=_D;coordinator=_D;session=_D;dataVersion=_D;keyCode=_D;publicKey=_D;need_login=_N;phone=_D;codeKey=_D;serialNo=_D;qrCodeSerial=_D;userInfo=_D;accountInfo=_D;powerUserList=_D;doorAccountDict={};cookie=[];timestamp=int(time.time()*1000);accessToken=_D;refreshToken=_D;token=_D;expirationDate=_D;refresh_interval=8;is_debug=_N;shown_notification=_N
	def __init__(A,hass,config=_D):
		B=config;A.hass=hass
		if B is not _D:
			try:
				A.keyCode=B[_A9];A.publicKey=B[_AR];A.accessToken=B[_Ak];A.refreshToken=B[_Al];A.token=B[_AA];A.userInfo=B[_AS];A.powerUserList=B[_AT];A.doorAccountDict=B[_Am];A.is_debug=B['is_debug'];A.dataVersion=B[_An];A.account=B[_j];A.password=B[_AF];A.refresh_interval=B[_Ao]
				if A.refresh_interval<8:A.refresh_interval=8
			except Exception as C:LOGGER.error(C)
	async def save_data(B):A={};A[_A9]=B.keyCode;A[_AR]=B.publicKey;A[_Ak]=B.accessToken;A[_Al]=B.refreshToken;A[_AA]=B.token;A[_AS]=B.userInfo;A[_AT]=B.powerUserList;A[_Am]=B.doorAccountDict;A['is_debug']=B.is_debug;A[_An]=VERSION;A[_j]=B.account;A[_AF]=B.password;A[_Ao]=B.refresh_interval;await async_save_to_store(B.hass,'state_grid.config',A)
	def encrypt_post_data(A,data):B={'_access_token':A.accessToken[len(A.accessToken)//2:]if A.accessToken else'','_t':A.token[len(A.token)//2:]if A.token else'','_data':data,_s:A.timestamp};return A.encrypt_wapper_data(B)
	def encrypt_wapper_data(A,data):B=a(json_dumps(data),A.keyCode);return{_A:B+c(B+str(A.timestamp)),'skey':d(A.keyCode,A.publicKey),_s:str(A.timestamp)}
	def handle_request_result_message(E,api,result,printResult=_V):
		D='message';C='resultMessage';A=result
		if E.is_debug and printResult:LOGGER.warning(api+'-'+json_dumps(A))
		B=_D
		if _A in A and A[_A]and _f in A[_A]and C in A[_A][_f]:B=A[_A][_f][C]
		elif _f in A and C in A[_f]:B=A[_f][C]
		elif D in A:B=A[D]
		else:B=json_dumps(A)
		return B
	async def __fetch_safe(A,api,data):
		B=await A.__fetch(api,data)
		if _I not in B:return B
		if A.__need_login(B[_I]):
			await A.__try_password_login()
			if A.need_login is _N:return await A.__fetch(api,data)
			if A.need_login is _V:A._show_token_notification()
			return B
		else:return B
	def __need_login(B,code):
		A=code
		if 10015==A or 10108==A or 10009==A or 10207==A or 10005==A or 10010==A or 30010==A or 10002==A:B.need_login=_V;return _V
		return _N
	async def __try_password_login(A):
		B=await A.password_login(A.account,A.password,_V,3)
		if _G in B and B[_G]==0:A.need_login=_N;A.shown_notification=_N;await A.save_data()
	async def __fetch(A,api,data,header=_D):
		R='encryptData';Q='client_secret';P='application/json;charset=UTF-8';O='Content-Type';M=header;J='client_id';D=api;A.timestamp=int(time.time()*1000);E=A.timestamp
		if A.keyCode is _D:A.keyCode=e(32,16,2)
		G=A.keyCode;F={'Accept':P,O:P,'version':'1.0',_E:'0901',_s:str(E),'wsgwType':'web','appKey':appKey};C=data
		if D==get_request_key_api:C={J:appKey,Q:appSecret};H=a(json_dumps(C),G);C={_A:H+c(H+str(E)),'skey':d(G,'042D12DFBC179202AC4B7B7BADCDA6FF7B604339263F6AB732CE7107B7EA3830A2CA714DC303920D3CFF7647D898F1A8CC6C24E9EC3CC194E22D984AF7E16B42DC'),J:appKey,_s:str(E)}
		elif D==get_request_authorize_api:
			C={J:appKey,'response_type':_I,_Ap:'/test',_s:E,'rsi':A.token};C=urllib.parse.urlencode(C);F[O]='application/x-www-form-urlencoded; charset=UTF-8';F[_A9]=G;K=async_get_clientsession(A.hass,_N)
			async with K.post(baseApi+D,data=C,headers=F)as L:B=await L.json();B=b(B[_A],A.token);B=json.loads(B);return B
		elif D==get_web_token_api:C={'grant_type':'authorization_code','sign':c(appKey+str(E)),Q:appSecret,'state':'464606a4-184c-4beb-b442-2ab7761d0796','key_code':G,J:appKey,_s:E,_I:C[_I]};H=a(json_dumps(C),G);C={_A:H+c(H+str(E)),'skey':d(G,A.publicKey),_s:str(E)}
		else:C=A.encrypt_post_data(C)
		if M is not _D:F.update(M)
		if D in sessionIdControlApiList:F['sessionId']='web'+str(E)
		if D in keyCodeControlApiList:F[_A9]=G
		if D in authControlApiList:F['Authorization']='Bearer '+A.accessToken[:len(A.accessToken)//2]
		if D in tControlApiList:F['t']=A.token[:len(A.token)//2]
		I=0
		while I<MAX_RETRIES:
			try:
				K=async_get_clientsession(A.hass,_N)
				async with K.post(baseApi+D,json=C,headers=F)as L:
					B=await L.text()
					if B.startswith('{'):
						B=json.loads(B)
						if R in B:B=b(B[R],G);B=json.loads(B)
					return B
			except Exception as N:
				LOGGER.error(f"请求错误: {N}. 尝试第 {I+1} 次重试...");I+=1
				if I==MAX_RETRIES:raise N
	async def __get_request_key(A):
		A.keyCode=_D;B=await A.__fetch(get_request_key_api,{});C=A.handle_request_result_message('get_request_key_api',B)
		if B[_I]==_F:A.keyCode=B[_A][_A9];A.publicKey=B[_A][_AR];return{_G:0}
		return{_G:1,_y:C}
	async def __get_pass_verify_code(B,account,password):
		C={_j:account,_AF:password,'canvasHeight':200,'canvasWidth':310};A=await B.__fetch(get_verify_code_api,C);D=B.handle_request_result_message('get_verify_code_api',A,_N)
		if _I in A and A[_I]==1 and _A in A:B.ticket=A[_A]['ticket'];return{_G:0,_AU:A[_A][_AU],_AV:A[_A][_AV],_AW:A[_A][_AW]}
		return{_G:1,_y:D}
	async def __verify_password(B,account,password,code,loginKey):
		C={'loginKey':loginKey,_I:code,'params':{_Q:{_m:'',_o:_AN,_l:_M,_n:''},_AX:{'optSys':'ios','pushId':'00000','addressProvince':'110100',_AF:password,'addressRegion':'110101',_j:account,'addressCity':'330100'}},'Channels':'web'};A=await B.__fetch(verify_password_api,C);D=B.handle_request_result_message('verify_password_api',A)
		if A[_I]==1:
			if A[_A]and A[_A][_f]and A[_A][_f]['resultCode']=='0000':B.token=A[_A][_AG][_AA];B.userInfo=A[_A][_AG][_AS][0];return{_G:0}
		return{_G:1,_y:D}
	async def __get_request_authorize(B):
		A=await B.__fetch(get_request_authorize_api,{});E=B.handle_request_result_message('get_request_authorize_api',A)
		if _I in A and A[_I]==_F:C=A[_A][_Ap];D=C.rfind('code=');B.authorizeCode=C[D+5:D+5+32];return{_G:0}
		return{_G:1,_y:E}
	async def __get_web_token(A):
		C={_I:A.authorizeCode};B=await A.__fetch(get_web_token_api,C);D=A.handle_request_result_message('get_web_token_api',B)
		if _I in B and B[_I]==_F:A.accessToken=B[_A]['access_token'];A.refreshToken=B[_A]['refresh_token'];return{_G:0}
		return{_G:1,_y:D}
	async def __get_door_number(A):
		B=configuration[_Ac];G={_C:B[_C],_E:B[_E],_T:B[_T],_Q:{_l:B[_Q][_l],_m:B[_Q][_m],_n:B[_Q][_n],_o:B[_Q][_o]},_AX:{_W:A.userInfo[_W]},_AA:A.token};C=await A.__fetch_safe(get_door_number_api,G);H=A.handle_request_result_message('get_door_number_api',C)
		if _I in C and str(C[_I]) in ('1', '0000', '000000') and _A in C and _AG in C[_A]:
			E={}
			if A.powerUserList is not _D:E={A[_g]:A for A in A.powerUserList}
			F=[]
			for D in C[_A][_AG][_AT]:
				if D[_g]in E:F.append(E[D[_g]])
				elif _AY in D and D[_AY]!='05':F.append(D)
			A.powerUserList=F;return{_G:0}
		return{_G:1,_y:H}
	async def __get_door_balance(C,door_account):
		A=door_account;E={_A:{_L:'',_O:'',_H:configuration[_j][_H],_B:configuration[_j][_B],_AH:C.userInfo[_W],_AI:C.userInfo.get(_Aa,C.userInfo.get('nickname',_D)),_R:_F,_b:_F,_AZ:C.userInfo[_W],_AB:[{'consNoSrc':A[_g],_Ab:A.get(_X,A.get(_AJ,_D)),'sceneType':A.get('consSortCode',A.get(_AY,_D)),_AC:A[_AC],_h:A[_h]}]},_C:'0101143',_E:configuration[_E],_T:A.get(_X,A.get(_AJ,_D))};B=await C.__fetch_safe(get_door_balance_api,E);C.handle_request_result_message('get_door_balance_api',B)
		if _I in B and str(B[_I]) in ('1', '000000') and _A in B and B[_A]and _AB in B[_A]:
			D=B[_A][_AB]
			if len(D)!=0:A[_Y]=D[0]
	async def __get_door_bill(C,door_account,year):
		F='dataInfo';D='mothEleList';A=door_account;G={_A:{_AH:C.userInfo[_W],_H:configuration[_H],_c:'11',_AK:A[_As],_B:'ALIPAY_01',_h:A[_h],_Ab:A[_X],_b:_F,_R:_F,_O:'',_L:'',_AI:'',_Aq:A[_X],_AZ:C.userInfo[_W],_AC:A[_g],_Ar:year},_C:_x,_E:_w,_T:A[_X]};B=await C.__fetch_safe(get_door_bill_api,G);C.handle_request_result_message('get_door_bill_api',B)
		if _I in B and str(B[_I]) in ('1', '000000') and _A in B and B[_A]:
			if D in B[_A]:
				if _S not in A:A[_S]=B[_A][D]
				else:
					H={A[_Z]:A for A in A[_S]};I=B[_A][D]
					for E in I:
						if E[_Z]not in H:A[_S].append(E)
			if F in B[_A]:return B[_A][F]
	async def __get_door_mouth_bill(F,door_account,monthBill):
		M='billRead';J=monthBill;G='pointList';E='readList';C=door_account;K=datetime.datetime.strptime(J[_Z],'%Y%m');N=f"{K.year}-{K.month:02d}";O={_A:{_H:configuration[_k][_H],_B:configuration[_k][_B],_R:configuration[_k][_R],_c:configuration[_k][_c],_AC:C[_g],_b:C[_X],_h:C[_h],'queryDate':N,_Aq:C[_X],_AK:C[_As],_AZ:F.userInfo[_W],_O:'',_L:'',_AI:F.userInfo[_Aa],_AH:F.userInfo[_W]},_C:configuration[_k][_C],_E:configuration[_k][_E],_T:C[_X]};B=await F.__fetch(get_door_ladder_api,O);Q=F.handle_request_result_message('get_door_ladder_api',B)
		if _I in B and str(B[_I]) in ('1', '000000') and _A in B and B[_A]and _AB in B[_A]:
			A=B[_A][_AB][0];H=0;L=0;D=[]
			if E in A and len(A[E])>0:D=A[E]
			elif G in A and len(A[G])>0 and E in A[G][0]and len(A[G][0][E])>0:D=A[G][0][E]
			if len(D)>0:
				L=catchFloat(D[0],'activeCount')
				if M in D[0]:
					for P in D[0][M]:H=max(H,catchInt(P,'currentNumber'))
			I={};I[_At]=H;I[_AD]=normal_round(L,2);J[_AL]=I
	async def __get_door_daily_bill(E,door_account,year,start_date,end_date,monthBill=_D):
		F='sevenEleList';D=monthBill;C=door_account;L={'params1':{_C:configuration[_C],_E:configuration[_E],_T:configuration[_T],_Q:{_l:configuration[_Q][_l],_m:configuration[_Q][_m],_n:configuration[_Q][_n],_o:configuration[_Q][_o]},_AX:{_W:E.userInfo[_W]},_AA:E.token},'params3':{_A:{_AH:E.userInfo[_W],_AC:C[_g],_AK:_a,'endTime':end_date,_h:C[_h],_Ar:year,_Ab:C.get(_X,C.get(_AJ,_D)),_O:'',_L:'','startTime':start_date,_AI:E.userInfo[_Aa],_B:configuration[_d][_B],_H:configuration[_d][_H],_c:configuration[_d][_c],_b:configuration[_d][_b],_R:configuration[_d][_R]},_C:configuration[_d][_C],_E:configuration[_d][_E],_T:C.get(_X,C.get(_AJ,_D))},'params4':'010103'};B=await E.__fetch_safe(get_door_daily_bill_api,L);E.handle_request_result_message('get_door_daily_bill_api',B)
		if _I in B and str(B[_I]) in ('1', '000000') and _A in B and B[_A]and F in B[_A]:
			if D is _D:C[_i]=B[_A][F]
			else:
				G=0;H=0;I=0;J=0;K=0
				for A in B[_A][F]:A[_t]=catchFloat(A,_t);A[_z]=catchFloat(A,_z);A[_A0]=catchFloat(A,_A0);A[_A1]=catchFloat(A,_A1);A[_A2]=catchFloat(A,_A2);G+=A[_t];H+=A[_z];I+=A[_A0];J+=A[_A1];K+=A[_A2]
				D[_AD]=normal_round(G,2);D[_A3]=normal_round(H,2);D[_A4]=normal_round(I,2);D[_A5]=normal_round(J,2);D[_A6]=normal_round(K,2);D[_Au]=B[_A][F]
	async def password_login(B,account,password,encode=_N,retry=0):
		L=retry;E=account;C=password
		if encode==_N:C=hashlib.md5(C.encode()).hexdigest().upper()
		M=_D;A=await B.__get_request_key()
		if _G in A and A[_G]!=0:return A
		A=await B.__get_pass_verify_code(E,C)
		if _G in A and A[_G]!=0:return A
		N=int(A[_AW]);O=0;P=base64_image_to_bytes(A[_AV])
		with Image.open(io.BytesIO(P))as F:G,H=F.size;O=H
		Q=base64_image_to_bytes(A[_AU])
		with Image.open(io.BytesIO(Q))as F:G,H=F.size;R=F.crop((0,N,G,N+O));D=R.point(lambda p:255 if p>150 else 0)
		G=D.width;H=D.height;I=[[0 for A in range(H)]for A in range(G)]
		for J in range(D.height):
			for K in range(D.width):
				S=D.getpixel((K,J))
				if is_dark(S,100):I[K][J]=1
				else:I[K][J]=0
		T,U,V,W=find_max_rectangle(I);M=T;A=await B.__verify_password(E,C,M,B.ticket)
		if _G in A and A[_G]!=0:
			if L<=0:return A
			else:
				LOGGER.error('国家电网 - 账号密码登录失败，将重试！');A=await B.password_login(E,C,L-1)
				if _G in A and A[_G]!=0:return A
		B.account=E;B.password=C;return await B.__get_token()
	async def __get_token(B):
		A=await B.__get_request_authorize()
		if _G in A and A[_G]!=0:return A
		A=await B.__get_web_token()
		if _G in A and A[_G]!=0:return A
		B.need_login=_N;await B.save_data();return{_G:0}
	def _show_token_notification(A):
		if A.shown_notification==_V:return
		A.shown_notification=_V;B='国家电网登录失败，将在下个轮询重试';persistent_notification.create(A.hass,B,title='国家电网 - 登录失败');LOGGER.error(B)
	async def refresh_data(C,force_refresh=_N):
		A5='recent_12_monthly_ele_list';A4='recent_30_daily_ele_list';A3='monthEleCost';A2='last_month_ele_cost';A1='year_ele_cost';A0='%Y%m%d';z='daily_lasted_date';y='isMent';f=force_refresh;e='monthEleNum';d='last_month_ele_num';T='year_ele_num';S='yearTotalCost';R='day';J='year_bill_list';I='balance'
		try:
			if f:await C.__get_door_number()
			A6=f or int(time.time()*1000)-C.timestamp>C.refresh_interval*3600*1000
			if A6 is _N:return
			H=datetime.datetime.now();D=H-datetime.timedelta(days=1);U=f"{D.year}-{D.month:02d}-{D.day:02d}";F=D-datetime.timedelta(days=40);V=f"{F.year}-{F.month:02d}-{F.day:02d}"
			for A in C.powerUserList:
				A7=A[_g];C.doorAccountDict[A7]=A;await C.__get_door_balance(A)
				if C.need_login is _V:return
				if _Y in A:
					g=catchFloat(A[_Y],'accountBalance');AB=catchFloat(A[_Y],'estiAmt');AC=catchFloat(A[_Y],'prepayBal');W=catchFloat(A[_Y],'sumMoney');AD=catchFloat(A[_Y],'historyOwe');h=A[_Y][_AK];i=''
					if y in A[_Y]:i=A[_Y][y]
					A8=h==_F;X=h=='0';j=not(not X or i!=_F)
					if A8:A[I]=W
					if X and not j:A[I]=-abs(W)
					if X and j:A[I]=W
					if g!=0:A[I]=g
				else:LOGGER.error('国家电网账户余额获取失败！')
				if I not in A:A[I]=0
				await C.__get_door_daily_bill(A,H.year,V,U)
				print("【调试】get_door_daily_bill_api 返回：", A.get(_i))
				if _i not in A:LOGGER.error('国家电网无法获取日用电数据！');continue
				Y=0;K=_N
				for k in range(10):
					E=A[_i][k]
					try:float(E[_t]);K=_V;break
					except:Y=Y+1
				l=0;m=0;n=0;o=0;p=0;A[z]=f"{H.year}-{H.month:02d}-{H.day:02d}"
				if K:
					for k in range(Y):A[_i].pop(0)
					E=A[_i][0];G=datetime.datetime.strptime(E[R],A0);A[z]=f"{G.year}-{G.month:02d}-{G.day:02d}";l=catchFloat(E,_t);m=catchFloat(E,_z);n=catchFloat(E,_A0);o=catchFloat(E,_A1);p=catchFloat(E,_A2)
				A['daily_ele_num']=normal_round(l,2);A['daily_p_ele_num']=normal_round(m,2);A['daily_v_ele_num']=normal_round(n,2);A['daily_n_ele_num']=normal_round(o,2);A['daily_t_ele_num']=normal_round(p,2);q=0;r=0;s=0;t=0;u=0
				if K:
					for B in A[_i]:
						A9=datetime.datetime.strptime(B[R],A0)
						if A9.month!=G.month:break
						q+=catchFloat(B,_t);r+=catchFloat(B,_z);s+=catchFloat(B,_A0);t+=catchFloat(B,_A1);u+=catchFloat(B,_A2)
				A[_AD]=normal_round(q,2);A[_A3]=normal_round(r,2);A[_A4]=normal_round(s,2);A[_A5]=normal_round(t,2);A[_A6]=normal_round(u,2)
				if K:
					Z=G-datetime.timedelta(days=G.day)
					if _S not in A or len(A[_S])<12:await C.__get_door_bill(A,Z.year-1)
					v=await C.__get_door_bill(A,Z.year)
					if v is not _D:A[S]=v
					w=[]
					if _S in A:
						for B in A[_S]:
							if _AL not in B:await C.__get_door_mouth_bill(A,B)
							if _Au not in B:AA,F,D=get_month_date_range(B[_Z]);U=f"{D.year}-{D.month:02d}-{D.day:02d}";V=f"{F.year}-{F.month:02d}-{F.day:02d}";await C.__get_door_daily_bill(A,int(AA),V,U,B)
							if B[_Z].startswith(str(Z.year)):w.append(B)
					A[J]=sorted(w,key=lambda x:x[_Z],reverse=_V)
				if S in A:A[T]=catchFloat(A[S],'totalEleNum');A[A1]=catchFloat(A[S],'totalEleCost')
				if T not in A:A[T]=0;A[A1]=0
				x=0;a=D
				if J in A and len(A[J])>0:
					L=A[J][0];A[d]=catchFloat(L,e);A[A2]=catchFloat(L,A3)
					if _AL in L:x=L[_AL][_At]
					a=datetime.datetime.strptime(L[_Z],'%Y%m')
				if d not in A:A[d]=0;A[A2]=0
				A['last_month_meter_num']=int(x);M=0;N=0;O=0;P=0;Q=0
				if a.month==12:M=A[_AD];N=A[_A3];O=A[_A4];P=A[_A5];Q=A[_A6]
				else:
					if J in A:
						for B in A[J]:M+=catchFloat(B,e);N+=B[_A3];O+=B[_A4];P+=B[_A5];Q+=B[_A6]
					if K and G.month!=a.month:M+=A[_AD];N+=A[_A3];O+=A[_A4];P+=A[_A5];Q+=A[_A6]
				A[T]=normal_round(M,2);A['year_p_ele_num']=normal_round(N,2);A['year_v_ele_num']=normal_round(O,2);A['year_n_ele_num']=normal_round(P,2);A['year_t_ele_num']=normal_round(Q,2)
				if _i in A:
					b=[]
					for B in A[_i][:30]:b.append({R:B[R],'ele':normal_round(catchFloat(B,_t),2),'v_ele':normal_round(catchFloat(B,_A0),2),'p_ele':normal_round(catchFloat(B,_z),2),'n_ele':normal_round(catchFloat(B,_A1),2),'t_ele':normal_round(catchFloat(B,_A2),2)})
					b.reverse();A[A4]=b
				else:A[A4]=[]
				if _S in A:
					A[_S]=sorted(A[_S],key=lambda x:x[_Z],reverse=_V);c=[]
					for B in A[_S][:12]:c.append({_Z:B[_Z],'cost':normal_round(catchFloat(B,A3),2),'ele':normal_round(catchFloat(B,e),2),'v_ele':B[_A4],'p_ele':B[_A3],'n_ele':B[_A5],'t_ele':B[_A6]})
					c.reverse();A[A5]=c
				else:A[A5]=[]
				A['refresh_time']=datetime.datetime.strftime(H,'%Y-%m-%d %H:%M:%S')
			await C.save_data()
		except:return 0
	def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict
