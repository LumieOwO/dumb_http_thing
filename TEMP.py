from methods import head

if __name__ == '__main__':
    url="http://data.pr4e.org/romeo.txt"
    response = head.Head(
        url=url,
        headers={}
    ).return_all()
    print(response.status_code)
    print(response.response)