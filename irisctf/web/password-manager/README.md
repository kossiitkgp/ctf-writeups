# Password Manager

Points: 50

> It looks like skat finally remembered to use his password manager! One small problem though, he forgot his password to the password manager!
> 
> Can you help him log back in so he can get back to his favorite RF forums?

`Author: User9684`

---

We are given `main.go` which once you read carefully tells us that
it takes the path to a file from the URL and serves the file in that location
from the file system. We also know that the `users.json` is just outside the
folder that the server looks in, so if we were to pass something like `../users.json` 
we would essentially solve the challenge

*Initially however I noticed that we were given the URL and passwd to the MySQL db they were using and had
the stupid idea that maybe I could connect to it from my laptop. This would obviously not work
since they were using a properly configured web server, however the command I used for this is below*

```sh
mysql -u readonly_user -p -h https://password-manager-web.chal.irisc.tf -P
 3306 uwu
```

We are also given this nice hint in the code 
```
// You. Shall. Not. Path traverse!
```

However it is not so simple. 

```go
var PathReplacer = strings.NewReplacer(
	"../", "",
)

path := PathReplacer.Replace(r.URL.Path)
```

The entire point of this section is to remove "../" from your URL, making your job harder.

Now at this point I had a brain fart. I was thinking if I pass `%2e%2e%2f` 
(the URL encoding for `../`) I could bypass the check, however this would obviously not work
because the URL encoding/decoding is happening by the browser itself, nothing to do with the server. And 
even if it was, after decoding its still going to be removed by the server.

I didn't have this clarity then, so I just kept sinking further. I found a tool called `[dotdotpwn](https://github.com/wireghoul/dotdotpwn)` 
that was supposed to be for finding path traversal vulnerabilities. But, as always, setup issues. 

Finally a while later [@harshkhandeparker](https://github.com/harshkhandeparkar) came online and solved it
with a crafted payload that would simplify to `../` after the check. 

```
https://password-manager-web.chal.irisc.tf/.../...//users.json
```

Later I saw a writeup that said they simply did `....//users.json` and that worked too

---

```sh
flag{}
```
