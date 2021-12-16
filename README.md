# Mini-Wallet-Exercise
     REST API with Framework FAST API with dummy data
### Clone Repository
``` git clone https://github.com/gofurmzq/Mini-Wallet-Exercise.git```
### Create log directory if doesn't exist
- mkdir logs/mini_wallet_api_error.log
- mkdir logs/mini_wallet_api_info.log
- mkdir logs/mini_wallet_api_warning.log

### Create .env file if doesn't exists
```nano .env```

### Rewrite .env file with the following value:

```
DEBUG=True
PORT=5001
WORKERS=4
LOG_TO_FILE=True

SECRET_KEY=b7f60c46f7c3982cb13bf20faae218ddc9ab4f92622163b9

ENABLE_APIDOCS=True
```


### Create virtualenv and activate virtual environment
```
python3.8 -m venv env
source env/bin/activate
```

### Install packages
```pip install -r requirements.txt```

### Run in terminal
```uvicorn app:app```

### See the swagger docs in browser :
```http://127.0.0.1:8000/api/v1/wallet/docs```

## HOW TO TESTING ONE BY ONE THE END POINT :

1. Initialize Account
   ```
   Request body : 
    {
        "customer_xid": "ea0212d3-abd6-406f-8c67-868e814a2436"
    }
    ```
2. View Balance
    
    Authorize : 
    ```
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXQiOnsiaWQiOiJjNGQ3ZDYxZi1iNzAyLTQ0YTgtYWY5Ny01ZGJkYWZhOTY1NTEiLCJvd25lZF9ieSI6IjZlZjMxOTc1LTY3YjAtNDIxYS05NDkzLTY2NzU2OWQ4OTU1NiIsInN0YXR1cyI6ImVuYWJsZWQiLCJlbmFibGVkX2F0IjoiMTk5NC0xMS0wNVQwODoxNTozMC0wNTowMCIsImJhbGFuY2UiOjB9fQ.8dnSsRAHyfqFYP6nQlH86O-hMZ3jJBvCehW4BrCT1Uo
    ```
3. Enable Account

   Authorize : 
   ```
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXQiOnsiaWQiOiI2ZWYzMWVkMy1mMzk2LTRiNmMtODA0OS02NzRkZGVkZTFiMTYiLCJvd25lZF9ieSI6ImM0ZDdkNjFmLWI3MDItNDRhOC1hZjk3LTVkYmRhZmE5NjU1MSIsInN0YXR1cyI6ImVuYWJsZWQiLCJlbmFibGVkX2F0IjoiMTk5NC0xMS0wNVQwODoxNTozMC0wNTowMCIsImJhbGFuY2UiOjB9fQ.mbRlEP3zJ5vd2IC4T7K8PH2uOtIrcntUBDKzZ3SR-Qw
   ```
4. Disable Account
   
   a. Request body : 
    ```
   {
       "is_disabled": "true"
   }
    ```
   b. Authorize : 
    ```
   eyJhbGciOiJIUzI1NiJ9.eyJ3YWxsZXQiOnsiaWQiOiI2ZWYzMWVkMy1mMzk2LTRiNmMtODA0OS02NzRkZGVkZTFiMTYiLCJvd25lZF9ieSI6IjUyNmVhOGIyLTQyOGUtNDAzYi1iOWZkLWYxMDk3MmUwZDZmZSIsInN0YXR1cyI6ImRpc2FibGVkIiwiZGlzYWJsZWRfYXQiOiIxOTk0LTExLTA1VDA4OjE1OjMwLTA1OjAwIiwiYmFsYW5jZSI6MH19.sN1nVYwTe1SqnXs9_qMQo2eeDbVo7qcJorqZG6C1azI
    ```
5. Add Virtual Money

    a.  Request body : 
    ```
    {
        "amount": 100000,
        "reference_id": "50535246-dcb2-4929-8cc9-004ea06f5241"
    }
    ```
    b. Authorize : 
    ```
    eyJhbGciOiJIUzI1NiJ9.eyJ3aXRoZHJhd2FsIjp7ImlkIjoiZWEwMjEyZDMtYWJkNi00MDZmLThjNjctODY4ZTgxNGEyNDMzIiwid2l0aGRyYXduX2J5IjoiNTI2ZWE4YjItNDI4ZS00MDNiLWI5ZmQtZjEwOTcyZTBkNmZlIiwic3RhdHVzIjoic3VjY2VzcyIsIndpdGhkcmF3bl9hdCI6IjE5OTQtMTEtMDVUMDg6MTU6MzAtMDU6MDAiLCJhbW91bnQiOiI2MDAwMCIsInJlZmVyZW5jZV9pZCI6ImM0Y2VlMDFmLTIxODgtNGEyOS1hYTlhLWNiN2ZiOTdkOGUwYSJ9fQ.BrVfxbg5ua9JW_-TZFYFgd3tcUuz4vr9cAZt2qK1Ths
    ```
6. Use Virtual Money

    a.  Request body : 
    ```
    {
        "amount": "60000",
        "reference_id": "4b01c9bb-3acd-47dc-87db-d9ac483d20b2"
    }
    ```
    b. Authorize :
    ```
    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXBvc2l0Ijp7ImlkIjoiZWEwMjEyZDMtYWJkNi00MDZmLThjNjctODY4ZTgxNGEyNDMzIiwiZGVwb3NpdGVkX2J5IjoiNTI2ZWE4YjItNDI4ZS00MDNiLWI5ZmQtZjEwOTcyZTBkNmZlIiwic3RhdHVzIjoic3VjY2VzcyIsImRlcG9zaXRlZF9hdCI6IjE5OTQtMTEtMDVUMDg6MTU6MzAtMDU6MDAifX0.RSUoj9na2Kke80sIUBug_xSLjtQOS57GmSc5RvYo0EM
    ```
#### NOTE: 
```
- I am still using data dummy for the token for testing the service cause i am not using Database or search engine
- If you wanna testing others router you may logout first cause each router have different dummy token
```

## License
 
This code is open source software licensed under the [Apache 2.0 License]("http://www.apache.org/licenses/LICENSE-2.0.html").
