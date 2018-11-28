API overview
============

<!-- ## Contents

- [Methods](#methods)
  - [Brand Registration](#accounts)
  - [Influencer Registration](#apps)
___ -->

## Methods

### Endpoints: 
    https://p1myy1ofs6.execute-api.us-west-2.amazonaws.com/default/login-auth-api/v1/login

###### Headers to set
    1. Content-Type = application/json

##### JSON Request Body
```
{
    "username": "john.doe@test.com",
    "password": "john.doe"
}
```
| Attribute                | Description                                                                        | Nullable |
| ------------------------ | ---------------------------------------------------------------------------------- | -------- |
| `email`                  | The email of the account                                                           | no       |
| `password`               | Password of account                                                                | no       |

##### JSON Response Body
```
{
    "headers": {
        "Content-Type": "application/json"
    },
    "statusCode": "200"
}
```
| Attribute                | Description                                                                        | Nullable |
| ------------------------ | ---------------------------------------------------------------------------------- | -------- |
| `status_code`            | status code of request                                                             | no       |


### Notes
```
{
  "body-json": {
    "username": "john.doe@test.com",
    "password": "john.doe"
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "647591104505",
    "resource-path": "/registration-auth-api/v1/influencer",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::647591104505:root",
    "request-id": "96c009f3-ec95-11e8-b448-c79a683c0ccf",
    "source-ip": "test-invoke-source-ip",
    "caller": "647591104505",
    "api-key": "test-invoke-api-key",
    "user-agent": "aws-internal/3 aws-sdk-java/1.11.447 Linux/4.9.124-0.1.ac.198.71.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192",
    "user": "647591104505",
    "cognito-identity-pool-id": "",
    "api-id": "qhoovbdv91",
    "resource-id": "6699eq",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}
```