---
title: "Unlocking free WiFi on British Airways"
reader_id: "01k906rcfy3p8c0zqsq3hz526c"
notion_page_id: "3484ebe7-f118-81c8-82b2-c9e91c49e3ac"
category: "article"
source_type: "Reader add from import URL"
reader_url: "https://read.readwise.io/read/01k906rcfy3p8c0zqsq3hz526c"
source_url: "https://news.ycombinator.com/item?id=45695134"
author: "vinhnx"
site: "ycombinator.com"
tags: []
published: "2025-10-24"
saved_at: "2025-11-01"
reading_time: "6 mins"
summary: "Users discuss tricks to bypass paid WiFi on planes and ships by tunneling or spoofing TLS/SNI. Some methods use proxies like Xray, DNS tunnels, or VPNs on common ports. Warnings note legal risks and that networks may patch these loopholes."
content_hash: "89deb843f81b029a3328c1ae7e928806b9655de756259d6d8df222cedea54aac"
---

# [vinhnx](<https://news.ycombinator.com/user?id=vinhnx>)

(2025-10-24 14:40:34)

## [tedggh](<https://news.ycombinator.com/user?id=tedggh>)

(2025-10-25 18:16:05)

Just a heads up before you attempt something like this. When on a plane, you may be subject to laws you don’t know or understand. In the US this could be considered tampering with the aircraft electronic systems and potentially send you to jail for many years. So if you don’t want to find out perhaps pay the $30 or whatever it is for Internet access.

## [markasoftware](<https://news.ycombinator.com/user?id=markasoftware>)

(2025-10-25 04:09:13)

I have a friend who did similar tunneling a while ago. It also works on cruise ships.

He discovered that on some airlines (I think American?), they use an advanced fortinet firewall that doesn't just look at the SNI -- it also checks that the certificate presented by the server has the correct hostname and is issued by a legit certificate authority.

My friend got around that restriction by making the tunnel give the aa.com SNI, and then forward a real server hello and certificate from aa.com (in fact I think he forwards the entire TLS 1.2 handshake to/from aa.com). But then as soon as the protocol typically would turn into encrypted application data, he ignores whatever he sent in the handshake and just uses it as an encrypted tunnel.

(The modern solution is just to use TLS 1.3, which encrypts the server certificate and hence prevents the firewall from inspecting the cert, reducing the problem back to just spoofing the SNI).

### [amritananda](<https://news.ycombinator.com/user?id=amritananda>)

(2025-10-25 06:18:53)

This is basically what Xray [1] does. For any connection request matching a particular SNI and not presenting a secret key, it proxies the entire SSL handshake and data to a camouflage website. Otherwise it can be used as a regular proxy disguised as SSL traffic to that website (with the camouflage website being set as the SNI host, so for all purposes legit traffic to that host for an external observer).

It's meant to get around the great firewall in China, so it has to avoid the GFW's active probers that check to make sure the external website is a (legit) host. However a friend was able to get it to work American's in-flight firewall if the proxy SNI is set to Google Analytics.

[1] <https://github.com/XTLS/Xray-core>

#### [filleokus](<https://news.ycombinator.com/user?id=filleokus>)

(2025-10-25 09:27:36)

Someone was using Xray, proxying to my employer, and it was detected in our attack surface management tool (Censys). I had some quite stressful few minutes before I realised what was going on, "how the hell have our TLS cert leaked to some random VPS hoster in Vietnam!?".

Thankfully for my blood pressure, whoever had set it up had left some kind of management portal accessible on a random high port number and it contained some strings which led me back to the Xray project.

### [josephg](<https://news.ycombinator.com/user?id=josephg>)

(2025-10-25 07:03:59)

> I have a friend who did similar tunneling a while ago. It also works on cruise ships.

Hah I was just about to say the same thing! I just got home from a ~3 week cruise. Internet on the ship was absurdly expensive ($50/day). And its weird - they have wifi and a phone app that works over the internet even if you don't pay. Google maps seemed to work. And my phone could receive notifications from apple just fine. But that was about it.

I spend some time staring at wireshark traces. It looks like every TCP connection is allowed to send and receive a couple packets normally. Then they take a close look at those packets to see if the connection should be allowed or blocked & reset. I'm not sure about other protocols, but for TLS, they look for a ClientHello. If preset, the domain is checked to see if its on a whitelist. Anything on their whitelist is allowed even if you aren't paying for internet. Whitelisted domains include the website of the cruise company and a few countries' visa offices. The cruise app works by whitelisting the company's own domain name. (Though I'm still not sure how my phone was getting notifications.)

They clearly know about the problem. There's some tools that make it easy to work around a block like this. But the websites for those tools are themselves blocked, even if you pay for internet. :)

If you figure out how to take advantage of this loophole, please don't abuse it too much or advertise the workaround. If it gets too well known or widely abused, they'll need to plug this little hole. And that would be a great pity indeed.

#### [walthamstow](<https://news.ycombinator.com/user?id=walthamstow>)

(2025-10-25 07:59:19)

$50 a day for internet is criminal, I don't care if you're at sea or in outer space.

#### [catgirlinspace](<https://news.ycombinator.com/user?id=catgirlinspace>)

(2025-10-25 07:31:33)

Perhaps they allowed Apple Push Notification service so their own app can receive notifications?

#### [CGamesPlay](<https://news.ycombinator.com/user?id=CGamesPlay>)

(2025-10-25 07:59:38)

I bet there some IT team at the cruise line that leaves these back doors in their systems deliberately as an “on-board activity” for their hacker customers.

### [7thpower](<https://news.ycombinator.com/user?id=7thpower>)

(2025-10-25 15:04:38)

I’m literally about to hop on a cruise ship tomorrow and trying to figure out how to solve for this, so this is timely.

#### [grogenaut](<https://news.ycombinator.com/user?id=grogenaut>)

(2025-10-25 17:25:17)

You could just relax and unplug

## [tgtweak](<https://news.ycombinator.com/user?id=tgtweak>)

(2025-10-25 04:34:49)

The amount of public WiFi's (including in-flight ones) I've bypassed by running a vpn server on udp port 53 is honestly insane. Sadly, this is becoming less commonplace many captive portals don't allow any egress at all aside from the captive portal's IP - but alas - still impressive how many are susceptible. It also bypasses traffic shaping (speed limiting) on most networks that are publicly accessible even if they do require some kind of authorization to enable external accessibility.

Highly recommend softether as they give you juicy Azure relay capability for free which is allowed in more "whitelist only" networks than your own vps server.

Haven't gone so far as to enable iodine for actual two-way dns communication through a third party DNS resolver, but that would probably work in more cases than this, albeit slower.

### [Nextgrid](<https://news.ycombinator.com/user?id=Nextgrid>)

(2025-10-25 08:22:03)

The networks where you can pay through the captive portal have to temporarily allow all traffic to load their payment widget and provide 3D-Secure (they don't know the domain your bank uses for that, so they have to allow all). Those can generally be bypassed by initiating the payment flow over and over again.

#### [jmkni](<https://news.ycombinator.com/user?id=jmkni>)

(2025-10-25 18:11:50)

Some implementations of 3d secure load in an iframe, and the containing app waits for a postMessage from inside the iFrame to confirm that 3d secure has completed successfully

If you can load your own content into the iframe, and can figure out what the containing page web app is expecting, you can send window.parent.postMessage() and bypass 3dsecure

### [treffer](<https://news.ycombinator.com/user?id=treffer>)

(2025-10-25 09:14:40)

I had 8 IPs in a hetzner server years ago. One IP had an iptables rule to accept openvpn on any port.

My openvpn config was a long list of commonly accepted ports on either tcp or udp.

Startup would take a while but the number of times it worked was amazing.

### [arch-choot](<https://news.ycombinator.com/user?id=arch-choot>)

(2025-10-25 06:39:55)

Yea, I run wireguard & OpenVPN on port53 (different VPS) just in case it works. Unfortunately my experience with the "pay to use" WiFi so far has been they validate that port 53 is valid DNS traffic, and often don't allow arbitrary resolvers (e.g. `dig example.com @1.1.1.1` will not work)

#### [geocar](<https://news.ycombinator.com/user?id=geocar>)

(2025-10-25 08:01:39)

You can use iodine and do a delegation from a real domain: It encodes packets in subdomains of your domain (and decodes them with a special DNS server). It is not fast.

I like to use SNI with e.g. pagead2.googlesyndication.com and www.googletagmanager.com because a lot of captive portals put ads on them, and I it on a google cloud instance since they own the IP.

There are more comments to this post:

  * <https://news.ycombinator.com/item?id=45702170>
  * <https://news.ycombinator.com/item?id=45700989>
  * <https://news.ycombinator.com/item?id=45701385>
  * <https://news.ycombinator.com/item?id=45701902>
  * <https://news.ycombinator.com/item?id=45703421>
  * <https://news.ycombinator.com/item?id=45701715>
  * <https://news.ycombinator.com/item?id=45701172>
  * <https://news.ycombinator.com/item?id=45702753>
  * <https://news.ycombinator.com/item?id=45703399>
  * <https://news.ycombinator.com/item?id=45704615>
  * <https://news.ycombinator.com/item?id=45704886>
  * <https://news.ycombinator.com/item?id=45701999>
  * <https://news.ycombinator.com/item?id=45701835>
  * <https://news.ycombinator.com/item?id=45701952>
  * <https://news.ycombinator.com/item?id=45702150>
  * <https://news.ycombinator.com/item?id=45701144>
  * <https://news.ycombinator.com/item?id=45700895>
  * <https://news.ycombinator.com/item?id=45701007>
  * <https://news.ycombinator.com/item?id=45701145>
  * <https://news.ycombinator.com/item?id=45701528>
  * <https://news.ycombinator.com/item?id=45700908>
  * <https://news.ycombinator.com/item?id=45701659>
  * <https://news.ycombinator.com/item?id=45702635>
  * <https://news.ycombinator.com/item?id=45702093>
  * <https://news.ycombinator.com/item?id=45703305>
