curl -X POST -d '{"username": "admin","password": "deco1234"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/api/auth/token/login/
curl -X GET http://127.0.0.1:8000/api/v1/friends/
curl -X GET http://127.0.0.1:8000/api/v1/friends/ -H 'Authorization: Token 099ab7cfff7a388d052092a99fa39a692f8cc20e'
curl -X GET http://127.0.0.1:8000/api/v1/belongings/ -H 'Authorization: Token 099ab7cfff7a388d052092a99fa39a692f8cc20e'
