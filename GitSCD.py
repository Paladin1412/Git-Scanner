__author__ = 'XiangHang'
#-*-coding:utf-8-*-

import requests

def verify(url):    
    if(url.startswith( 'http' or 'https')):
        try:
            status = ''
            dirconurl = url
            dirresponse=requests.get(dirconurl,verify=False,timeout=5)
            status=dirresponse.status_code
            gitpath = '/.git/config'
            giturl=url+'://'+gitpath.strip('\r\n')
            response=requests.get(giturl,timeout=5)
            if 'repositoryformatversion' in response.text:
                msg = 'Found /.git/config dir in url:'+giturl+''
                print(msg)               
                return True,url,msg
            else:
                msg = 'Cannot found /.git/config dir in url:'+giturl+''               
                return False,url,msg
        except Exception as e:
            msg = str(e)           
            return False,url,msg
    else:
        try:
            status = ''
            protocol = 'http'
            dirconurl = protocol + '://' + url
            dirresponse=requests.get(dirconurl,verify=False,timeout=5)
            status=dirresponse.status_code
            if (status < 400):                
                gitpath = '/.git/config'
                giturl=protocol+'://'+url+gitpath.strip('\r\n')
                response=requests.get(giturl,verify=False,timeout=5)
                if 'repositoryformatversion' in response.text:
                    msg = 'Found /.git/config dir in url:'+giturl+''
                    print(msg)               
                    return True,url,msg
                else:
                    msg = 'Cannot found /.git/config dir in url:'+giturl+''               
                    return False,url,msg
            else:
                gitpath = '/.git/config'
                giturl='https'+'://'+url+gitpath.strip('\r\n')
                response=requests.get(giturl,verify=False,timeout=5)
                if response.status_code < 400 and 'repositoryformatversion' in response.text:
                    msg = 'Found /.git/config dir in url:'+giturl+''
                    print(msg)               
                    return True,url,msg
                else:
                    msg = 'Cannot found /.git/config dir in url:'+giturl+''               
                    return False,url,msg
        except Exception as e:
            msg = str(e)           
            return False,url,msg

    
if __name__ == '__main__':

    def get_url_dict():
        pass_url = []
        with open('urls.txt','r') as f:
            for line in f.readlines():
                line = line.strip('\n')
                pass_url.append(line)
            f.close()
        return pass_url
    urls = get_url_dict()
    for url in urls:
        result = verify(url)
        data = open('data.txt','a+')
        print(result,file=data)
    data.close()