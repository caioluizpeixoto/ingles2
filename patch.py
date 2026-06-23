with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

pixel_code = """
<!-- FluxoFy & Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2434338437041148');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2434338437041148&ev=PageView&noscript=1"
/></noscript>
<!-- FluxoFy Tracking Integration -->
<script src="https://fluxo-track.vercel.app/fluxofy-pixel.js" data-product-id="c20dd07d-c97b-4bef-b267-f71143225c89" data-user-id="3f024dde-c859-4515-9d1e-9d1334447d61" data-ic-url="https://pay.wiapy.com/"></script>
<!-- End Pixel Code -->
"""

content = content.replace('</head>', pixel_code + '</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
