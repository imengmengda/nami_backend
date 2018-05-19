/auth/register
args:
{"username":"nami",
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

/auth/login/
args:
{"username":"nami",
"password":"python"}
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

/repo/add
args:
'{"name":"nami","secret":"python"}'
reply:
success:
{'status': 'success'}
fail:
{'error': 'repository nami exist'}

