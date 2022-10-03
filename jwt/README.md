
有关本文档的快速链接，请参考页面提示:

| 链接名称           | URL                                                                     | 内容说明                               |
|----------------|-------------------------------------------------------------------------|------------------------------------|
| GitHub MD 源代文件 | https://github.com/cwiki-us-docs/cwikius-docs/blob/master/jwt/README.md | 将本页面中的内容转换为 MD 文件的手册，并存于 Github 上面 |
| Docsify 转换后的手册 | https://cwiki-us-docs.github.io/cwikius-docs/#/jwt/README               | 将 MD 文件使用 Docsify 转换后的手册链接地址       |
| 问题讨论和社区        | https://www.ossez.com/tag/jwt                                           | 请访问使用 JWT 标签                       |
| CWIKI.US 页面链接  | https://www.cwiki.us/display/CWIKIUSDOCS/JWT+-+JSON+Web+Token           | Confluence 平台的原始翻译文件更新地址           |

**NEW:** 获得 [免费的 JWT 手册（JWT Handbook）](https://auth0.com/resources/ebooks/jwt-handbook) 同时学习更多有关 JWT 的内容！

## 什么是 JSON Web Token（JWT）

JSON Web Token (JWT) 作为一个开放的标准 ([RFC 7519](https://tools.ietf.org/html/rfc7519)) 定义了一种简洁自包含的方法用于通信双方之间以 JSON 对象的形式安全的传递信息。因为有数字签名，所以这些通信的信息能够被校验和信任。

JWT 可以使用秘钥（secret）进行签名 (使用 **HMAC** 算法) 或使用 **RSA** 或 **ECDSA** 算法的公钥/私钥对（public/private key）。

尽管 JWT 可以在通讯的双方之间通过提供秘钥（secret）来进行签名，我们将会更多关注 **已签名（signed）**的 token。 

通过签名的令牌可以验证其中数据的 *完整性（integrity）* ，而加密的令牌可以针对其他方 *隐藏（hide）* 申明。

当令牌（token）使用 公钥/私钥对（public/private key）进行签名的时候，只有持有私钥进行签名的一方是进行签名的。

### 关键术语的中英文对照
* token - 令牌
* secret - 秘钥
* signature - 签名
* claims - 要求或者数据


## 什么时候应该使用 JSON Web Tokens
在下面的一些场景中 JSON Web Tokens 可比较有用：

* **认证鉴权（Authentication）**： 这是 JWT 最常见的应用场景。一旦用户成功登入，在随后的每次请求中都将会包含JWT信息。 通过JWT的验证机制后，将允许该用户访问路由（routes）、服务（services）以及该Token所允许的资源。因为 JWT 的开销非常小，使其非常容易在跨域环境下使用，现如今 JWT 被广泛应用到单点登录（Single Sign On）中。

* **信息交换（Information Exchange）**： 因为 JSON Web Tokens 是可以进行签名的，因此 JWT 能够在不同系统之间安全的传递信息。 

例如基于使用公钥/私钥对（public/private key pairs），你可以确保请求的发送者是可信的。

同时，因为头部（header）和负载（payload）的信息和内容都参与了计算，所以你可以验证内容是否被篡改过。

## JSON Web Token 的结构是什么？
JSON Web Tokens 由使用  (`.`) 分开的 3 个部分组成的，这 3 个部分分别是：

- 头部（Header）
- 负载（Payload）
- 签名（Signature）

正是因为上面的组织形式，因此一个 JWT 通常看起如下面的表现形式。

`xxxxx.yyyyy.zzzzz`

让我们针对上面的形式来具体的分析下。

### 头部（Header）

在头部的数据中 *通常* 包含有 2 部分的内容：token 的类型，这里使用的是字符 JWT，和使用的的签名加密算法，例如 SHA256 或者 RSA。

例如下面的格式：

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```

然后，将上面的 JSON 数据格式使用 **Base64Url** 算法进行哈希，这样你就得到了 JWT 的第一部分。

### 负载（Payload）
JWT 的第二部分为负载，在负载中是由一些 claims 组成的。 Claims 是一些实体（通常指用户）和其他的一一些信息。

有下面 3 种类型的 claims *registered*， *public* 和 *private* 。

**[Registered claims](https://tools.ietf.org/html/rfc7519#section-4.1)**：这些 claims 是预先定义的，这些配置的内容不是必须的但是是推荐使用的，因此提供了一系列约定俗成使用的。比如：iss（issuer）， exp（expiration time）, sub（subject），aud（audience）和其他的一些更多的配置。

请注意，这些约定俗称的配置只有 3 个字符，以便于压缩数据量。


**[Public claims](https://tools.ietf.org/html/rfc7519#section-4.2)**：这些数据可以由使用 JWT 的用户自由去定义，但是为了避免冲突，你需要参考在 IANA JSON Web Token Registry  中对它们进行定义，或者将这些内容定义为 URI，并且需要避免可能出现的冲突。

**[Private claims](https://tools.ietf.org/html/rfc7519#section-4.3)**：这些内容是自定义的内容，这部分的内容被用于在数据传输短间进行转换的数据。这些数据是没有在  registered 和 public 中间没有定义的内容。

一个示例的负载：

````
{
"sub": "1234567890",
"name": "John Doe",
"admin": true
}
````

### 负载（payload）
中的数据也是经过 Base64Url  进行加密的，这部分加密的内容组成了 JWT 的第二部分。

请注意：针对令牌这部分的签名已经被防范篡改。但是这部分还是可以被解密的，因此请不要将任何密钥放到这部分的数据中，除非你的密钥是已经加密过的密钥。

### 签名（Signature）
为了创建一个加密部分，你需要有已经编码过的头部和负载，然后你还需要一个密钥（secret）和一个已经在头部中指定的加密算法来进行签名。

例如，如果你希望使用 HMAC SHA256 算法来进行签名，那么这个算法中使用的数据为：

````
HMACSHA256(
base64UrlEncode(header) + "." +
base64UrlEncode(payload),
secret)
````
签名的作用主要用于校验传输的令牌（Token）数据没有在过程中被篡改。

如果你的令牌是通过私有密钥进行签名的，那么也可以对 JWT 进行校验，以确定 JWT 的发送方使用是合法的签名。

## 将所有内容整合在一起

将这个 3 部分的内容使用 Base64-URL 编码后整合到一起，将每部分的数据直接使用 点号（.） 进行分隔，以确保令牌数据能够比较容易的在网络 HTTP 和 HTML 环境中进行传输。

针对使用 XML 的令牌，例如 SAML 来说，JWT 显得更加简洁和高效。

下面是使用了头部信息，负载信息和数字签名然后组合到一起的一个 JWT 令牌示例：

![encoded-jwt3|690x159](https://cdn.ossez.com/discourse-uploads/original/1X/121d022249f2480ae2f7d561c548b46964cd3541.png) 


如果你想使用 JWT，并且对一个已有的 JWT 令牌进行解密的话，你可以使用 https://jwt.io/#debugger-io 网站上提供的工具来对 JWT 字符串进行解密，校验和生产一个 JWT 令牌。

![legacy-app-auth-5|444x500](https://cdn.ossez.com/discourse-uploads/original/1X/6f26f249120d29f78d9b156df489c97c127a0d8f.png)

## JSON Web Tokens 是如何工作的
在用户权限校验的过程中，一个用户如果使用授权信息成功登录后，一个 JSON Web Token 将会返回给用户端。

因为返回的令牌包含有授权信息，应用程序应小心保存这些授权信息，以避免不必要的安全问题。你的应用程序在不需要授权信息的时候，应用程序不应该保留授权成功后返回的令牌。

应用程序也不应该将这些敏感信息保存在浏览器中，因为这样会更加容易导致信息泄漏，请参考链接：https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#local-storage 中的内容。

在任何时候，如果用户希望访问一个受保护的资源或者路由的时候，用户应该在访问请求中包含 JWT 令牌。通常这个令牌是存储在 HTTP 请求的头部信息，一般会使用 Authorization 字段，使用 Bearer 模式。

Http 头部发送给后台所包含的内容看起来如下所示：


    Authorization: Bearer <token>

在某些情况下，可以使用无状态的授权机制。服务器上受保护的路由将会检查随着访问提交的 JWT 令牌。如果令牌是有效的，用户将会被允许访问特定的资源。

如果 JWT 令牌中包含有必要的信息，服务器的服务端将不需要再次对数据库进行查询以加快访问速度。当然，不是所有的时候都可以这样进行处理。

当令牌随着头部中的 Authorization 信息一同发送，那么我们不需要使用 cookies，因此跨域访问（Cross-Origin Resource Sharing (CORS)）也不应该成为一个问题。

下面的示例图展示了JWT 是如何被获得的，同时也展示了 JWT 是如何被使用来访问服务器 API 的。

![client-credentials-grant|690x262](https://cdn.ossez.com/discourse-uploads/original/1X/f496687a5b020911f23e8facd5da5779d1a88a5b.png) 

1. 应用程序或者客户端，通过对授权服务器的访问来获得授权。这个可能有不同的授权模式。例如，通常我们可以使用 OpenID Connect 提供的标准的授权地址来进行授权，请参考链接：http://openid.net/connect/。通常来说一个标准的授权地址为 /oauth/authorize，并且使用下面类似的标准授权流程，请参考链接：http://openid.net/specs/openid-connect-core-1_0.html#CodeFlowAuth 中的内容。
2. 当授权完成后，授权服务器将会返回访问令牌（access token）给应用。
3. 应用使用获得的令牌来访问收到保护的资源（例如 API）等。

需要注意的是，通过使用了签名的令牌，尽管用户可能没有办法对使用的令牌进行修改，但是令牌中包含的所有信息将会暴露给用户或者其他的应用。因此，你不应该在你的令牌中存储密钥或者任何的敏感信息。


## 为什么我们需要使用 JSON Web Tokens

让我们讨论下 JSON Web Tokens (JWT) 针对  Simple Web Tokens (SWT) 和 Security Assertion Markup Language Tokens (SAML) 而言有什么优势吧。

相对 XML 来说，JSON 格式更加简洁，对 JSON 格式进行编码后的数据量更小，这就使得 JWT 相对 SAML 来说显得更加小巧，这使得 JWT 更加容易能够在 HTTP 和 HTML 环境之间传递数据。

在安全性上面，SWT 只能使用通过 HMAC 算法的对称方式签名。JWT 和 SAML 都可以使用基于 X.509 认证的公钥/私钥 密钥对的方式进行加密和解密。相比针对 JSON 格式的签名，针对XML 的数字签名更加容易导入安全漏洞。

在 JSON 格式的处理上，当前几乎所有的语言都能够支持和进行解析，这是因为 JSON 格式的数据更加容易映射到数据对象中。XML 则没有针对文本到对象的映射支持。这就导致了相对 SAML 来说，JWT 的处理更加容易。

在使用方面，JWT 已经被大量的在互联网上面取得了应用，针对多平台的使用上，JSON 格式在客户端上面更加容易被使用，尤其是针对移动平台。

针对 JSON 和 SAML 数据格式的内容对比，请参考下面的图片：

![comparing-jwt-vs-saml2|325x500](https://cdn.ossez.com/discourse-uploads/original/1X/54150ee8f3cba3b6afa81a1046ec400004fa3a34.png) 

从上面的图片的对比上，我们可以看到基于 JSON 格式的内容更少，表达性更好。

如果你希望了解更多有关 JSON Web Tokens 的使用，并且打算开始在你的系统中应用这种格式，请参考由 Auth0 官方提供的介绍和文档，访问链接是：http://auth0.com/learn/json-web-tokens。