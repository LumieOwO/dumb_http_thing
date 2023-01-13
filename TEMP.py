from methods import post

if __name__ == '__main__':
    url=""
    response = post.Post(
        url=url,
        headers={
        },
        payload = {
        }
    ).return_all()
    #print(response.status_code)
    #print(response.response)