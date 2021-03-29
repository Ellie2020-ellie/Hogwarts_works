ds = [
    {'platform': 'ANY',
     'browserName': "chrome",
     # 'version': '89',
     'javascriptEnabled': True
     },
    {
        "browserName": "firefox",
        "marionette": True,
        "acceptInsecureCerts": True,
    }
]
remote = 'http://localhost:4444/wd/hub'
