# GraphQL wrapper for a RESTful API

## Companion article
https://medium.com/@nderkach/how-to-build-a-graphql-wrapper-for-a-restful-api-in-python-b49767676630

## Usage
### Install dependencies and start the server
```
# Install Dependencies and export env variables
pipenv install
export AIRBNB_LOGIN='replace_with_your_login'
export AIRBNB_PASSWORD='replace_with_your_password'

# Run the server
pipenv run python server.py
```

### Go to the /graphql url
http://localhost:5000/graphql

### Sample Query
```json
{
  reviews(id:1238125) {
    comments
  }
}
```
