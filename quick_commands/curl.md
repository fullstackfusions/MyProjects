#### simple GET request

- curl https://api.example.com/data

#### GET request with headers

- curl -H "Authorization: Bearer YOUR_API_KEY" https://api.example.com/data

#### POST request with data

- curl -X POST https://api.example.com/data -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json"

#### PUT request to update data

- curl -X PUT https://api.example.com/data/123 -d '{"key1":"newvalue1", "key2":"newvalue2"}' -H "Content-Type: application/json"

#### DELETE request

- curl -X DELETE https://api.example.com/data/123

#### Sending form data

- curl -X POST https://api.example.com/form -d 'field1=value1&field2=value2'

#### Saving response to a file

- curl https://api.example.com/data -o filename.txt

#### Follow redirects

- curl -L https://api.example.com/data

#### Verbose outputs

- curl -v https://api.example.com/data

#### Sending cookies

- curl -b "name=value" https://api.example.com/data

#### Spcifying a user agent

- curl -A "MyUserAgent" https://api.example.com/data

#### Using proxy

- curl -x http://proxy-server:port https://api.example.com/data

#### Specify request timeout

- curl -m 10 https://api.example.com/data

#### Upload a file

- curl -X POST -F "file=@/path/to/file" https://api.example.com/upload

#### Download a file

- curl -O https://api.example.com/file

#### Use basic authentication

- curl -u username:password https://api.example.com/data

#### Resume a previous file transfer

- curl -C - -O https://api.example.com/file

#### SSL/TLS certificates

- curl -k https://api.example.com/data

#### Show response headers

- curl -I https://api.example.com/data

#### Use a custom certificate

- curl --cert /path/to/cert.pem https://api.example.com/data
