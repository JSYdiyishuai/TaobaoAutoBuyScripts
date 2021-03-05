# Taobao-AutoBuy
淘宝等网站抢购脚本（需chromedriver.exe）
查看chromedirver.exe版本：谷歌浏览器输入chrome://version
下载对应版本chromedriver.exe：http://chromedriver.storage.googleapis.com/index.html
解压文件，将chromedirver.exe放入$python-path$/chromedriver.exe 
如F:\python3.6.8\chromedriver.exe

# 淘宝抢购脚本                                                                                                   
## 使用方法：                                                                                                     
###     1、先将需要抢购的商品放到购物车中（注意购物车中只能放需要抢购的东西，到时抢购的时候会全部提交）；          
###     2、修改下本脚本中的BUY_TIME值，设定为需要抢购的时间，格式：20xx-x-x xx:xx:xx；                                                      
###     3、执行此脚本，然后等待浏览器打开弹出登陆界面，手机淘宝扫描登陆；                                          
###     4、脚本开始执行后，会定时刷新防止超时退出，到了设定时间点会自动尝试提交订单；                              
###     5、抢购时为了防止一次网络拥堵出问题，设置了尝试机制，会不停尝试提交订单，直到提交成功或达到最大重试次数为止#
###     6、脚本只负责提交订单，之后24小时内需要自行完成付款操作。                                                  
