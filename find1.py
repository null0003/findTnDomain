import requests


# coding = utf-8
import requests

# with open("domain.txt") as f:
# print()
with open("domain.txt") as f:
    # print(f.readlines()," 1111")
    for i in f.readlines():
        # print(str(i).strip(),"11")
        findDoman = str(i).strip()

        # url = "http://whois.ati.tn/index.php"
        #
        # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"domain\"\r\n\r\n%s \r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ext\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"" \
        #           "b_existe\"\r\n\r\nExiste3F\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW-- " %findDoman
        # headers = {
        #     'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        #     'cache-control': "no-cache",
        #     'postman-token': "0443e07f-be35-2c1f-c744-7036def84f87"
        # }
        #
        # response = requests.request("POST", url, data=payload, headers=headers)
        #
        #
        # print(findDoman, response.text.find("Nom Complet"))

        # open("result.txt", "a").writelines(findDoman + str(response.text.find("est libre pour l'instant."))+"\n")






        url = "https://www.quyu.net/domainchecker.php"

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data;" \
                  " name=\"token\"\r\n\r\n618425bfb760a07cf02a979d823a8dcdb30fd912\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n" \
                  "Content-Disposition: form-data; name=\"domain\"\r\n\r\n%s\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW" \
                  "\r\nContent-Disposition: form-data; name=\"tlds[]\"\r\n\r\n.st\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--" %findDoman
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "05d6797c-313c-d1e0-d39f-8ae53bc6dbd5"
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(findDoman,".st ",response.text.find("没有被注册，立即抢先注册"))
