from methods import Post
if __name__ == "__main__":
        post = Post(url='http://data.pr4e.org/romeo.txt', headers={},payload={})

        print(post.text)
        #print(post.response)
        #print(post.Allowed_METHODS)
        #print(post.return_all)
