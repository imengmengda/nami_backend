register interface:

    /auth/register
    method: POST
    args:
    {
        "username":"nami",
        "password":"python"}
    reply:
    success:
    {
        "token": "b'eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyNjc0NTI1MiwiZXhwIjoxNTI2NzQ1MjU0fQ.eyJpZCI6bnVsbH0._FWfrLmg4wsi3ZG6Vy54l4Kcc3R47kdP2qJWCB5hGJA'"
    }
    fail:
    {
        "error": "user exist"
    }
    curl demo:

login interface:

    /auth/login/
    args:
    {
        "username":"nami",
        "password":"python"
    }
    reply:
    success:
    {
      "token": "b'eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyNjc0NTI1MiwiZXhwIjoxNTI2NzQ1MjU0fQ.eyJpZCI6bnVsbH0._FWfrLmg4wsi3ZG6Vy54l4Kcc3R47kdP2qJWCB5hGJA'"
    }
    failed:
    {
      "error": "password error"
    }
    {
      "error": "user not exist"
    }

repository interface:

    /repo
    args:
    {
        "token": "xxx"
    }
    reply:
    seccess:
    {
      "repo": [
        {
          "create_time": "Sun, 20 May 2018 17:33:31 GMT",
          "owner_id": 1,
          "repo_name": "nami3",
          "url": "http://www.baidu.com"
        },
        {
          "create_time": "Sun, 20 May 2018 18:11:50 GMT",
          "owner_id": 1,
          "repo_name": "nami6",
          "url": "http://www.baidu.com"
        }
      ]
    }
    failed:
    {
        "repo": null
    }


    /repo/add
    args:
    {
        "name":"nami",
        "secret":"python"
        "token": "b'eyJhbGciOiJIUzI1NiIsImlhdCI6MTUyNjc0NTI1MiwiZXhwIjoxNTI2NzQ1MjU0fQ.eyJpZCI6bnVsbH0._FWfrLmg4wsi3ZG6Vy54l4Kcc3R47kdP2qJWCB5hGJA'"
    }
    reply:
    success:
    {
        'status': 'success'
    }
    fail:
    {
        'error': 'repository nami exist'
    }

commit interface:

    /commit/add
    args:
    {
        "repo_name":"nami3",
        "content":"first commit"
    }

    /commit
    args:
    {
        "token": "xxx"
    }
    reply:
    success:
    {
      "commit": [
        {
          "repo_id": 1,
          "update_time": "Sun, 20 May 2018 17:33:31 GMT"
        }
      ]
    }
    fail:
    {
      "commit": null
    }

