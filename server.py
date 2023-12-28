from flask import Flask, jsonify, request
import ssl

app = Flask(__name__)

@app.route('/api/user', methods=['GET'])
def get_user():
    response_data = {
        "status": "success",
        "code": 200,
        "data": {
            "id": 1000,
            "name": "user",
            "email": "user@gmail.com",
            "vip_until": "2030",
            "reg": "2023-12-30 12:12:12"
        }
    }

    headers = {
        "Date": "Sat, 30 Dec 2023 12:12:12 GMT",
        "Content-Type": "application/json",
        "X-Powered-By": "PHP/8.1.26",
        "Cache-Control": "no-cache, private",
        "X-Ratelimit-Limit": "60",
        "X-Ratelimit-Remaining": "59",
        "Access-Control-Allow-Origin": "*",
        "Vary": "Authorization,Accept-Encoding",
        "Cf-Cache-Status": "DYNAMIC",
        "Server": "cloudflare",
        "Cf-Ray": "83c9eb5688bd0490-CDG",
        "Alt-Svc": "h3=\":443\"; ma=86400"
    }

    return jsonify(response_data), 200, headers

if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=context)