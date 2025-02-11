import streamlit as st
from PIL import Image
import subprocess

st.title("一个大聪明的网站")

def page1():
    #文字
    st.header('这是我的兴趣推荐')
    st.video("fangzejin_超卡视频.mp4")
    st.write("你好,我叫方泽瑾,一个中雪参")
    st.write('我喜欢八卦，玩梗和恶搞别人（上面的视频没让你的设备卡住算你运气好）')
    st.write('要问我怎么体现')
    st.write('我：请看VCR(温馨提示：放大声音后口感更佳)')
    st.video("fangzejin_恶搞视频1.mp4")
    st.video("fangzejin_恶搞视频2.mp4")
    ag=st.selectbox("你被吓到了吗？",[" ","对","没有"])
    if ag =="对":
        st.image("fangzejin_奸笑.jpeg")
    if ag=="没有":
        st.write("你放屁")
        st.image("fangzejin_奸笑.jpeg")

def page2():
    st.header(":sunglasses:图片修改小程序:thumbsdown:")
    uploaded_file=st.file_uploader("图片上传",type=["jpg","jpeg","png"])
    if uploaded_file:
        tab1,tab2,tab3,tab4,tab5=st.tabs(["原图","改色","反色","物体拟人娘化走光图片","子家老师改色图片"])
        img=Image.open(uploaded_file)
        img1=Image.open("子家老师.png")
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,2,1,0))
        with tab3:
            st.image(img_fan(img))
        with tab4:
            st.write("她们都走光了，一个也没留下")
            st.write("不在下面")
            for i in range(400):
                st.write("       ")
            st.write(":grin:我都说了不在下面，你还偏不信   joker:point_right:你")
            aaa=st.text_input("你想对我说什么")
            if aaa:
                st.write("不许说脏话")
                
        with tab5:
            st.image(img_change(img1,1,2,0))

def page3():
    st.header("智慧词典")
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list=f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
        
    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list=f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
        
    word=st.text_input("请输入您想要查询的单词")
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
            
        with open("check_out_times.txt","w",encoding="utf-8") as f:
            message=""
            for k,v in times_dict.items():
                message+=str(k)+"#"+str(v)+"\n"
            message=message[:-1]
            f.write(message)
        
        st.write("查询次数：",times_dict[n])
        if word =="this":
            st.code('''
                    #恭喜你触发彩蛋
                    import this
                    ''')
        if word =="方泽瑾":
            st.balloons()
        if word =="侯代富":
            img1=Image.open("子家老师.png")
            st.image(img_change(img1,1,2,0))
        if word =="houdaifu":
            st.snow()
            img1=Image.open("子家老师.png")
            st.image(img_change(img1,1,2,0))



def page4():
    st.header("我的留言区")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        meassages_list=f.read().split("\n")
    for i in range(len(meassages_list)):
        meassages_list[i]=meassages_list[i].split("#")
        
    for i in meassages_list:
        if i[1]=="阿短":
            with st.chat_message("😄"):
                st.write(i[1],":",i[2])
        elif i[1]=="编程猫":
            with st.chat_message("👎"):
                st.write(i[1],":",i[2])
        else:
            st.write(i[1],":",i[2])
            
        
    name=st.text_input("你谁呀，你什么身份啊？")
    new_message=st.text_input("你要狗叫什么？")
    if st.button("发送"):
        meassages_list.append([str(int(meassages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message=""
            for i in meassages_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            f.write(message)
            
def page5():
    st.header("------------------火星踏步------------------")
    st.write("你好，你叫codemao（又称coldmao）")
    st.write("你是第一个登陆火星的地球生物")
    st.write("但因为你也是高等智慧生命体")
    st.write("所以总部给你布置了任务：寻找冰")
    st.write("你降落在了南极的艾托肯盆地")
    st.write("在任务的最后一天，你发现了一个洞穴")
    st.write("你走了进去，发现里面有三层天然冰")
    st.write("可你脚下一滑，掉在了冰上")
    st.write("幸好你带了飞索")
    st.write("可飞梭启动后突然出现了问题")
    st.write("修复需要60秒的时间")
    st.write("你焦急不堪")
    st.write("突然，一股强大的源码之力飞进了你的体内")
    st.write("你的脑海里响起了一个声音")
    st.write("“你做的已经很不错了，接下来浇给无敌的老师吧”")
    st.write("-------------------操作说明------------------")
    st.write("上下左右键移动，碰到空位减一层")
    st.write(" ")
    st.write("那么接下来，坚持这漫长的60秒吧")
    st.write(" ")
    st.write("此为老版本，剧情与游戏有些许欠缺，不符，请谅解")
    
    if st.button("开始"):
        subprocess.run('疯狂的地板.exe')   

def page6():
    chengji=0
    st.header("网络梗考试")
    st.subheader("一、听力题（共2题，每题10分）(只有视频，自己听)")
    st.write("1.听到这个声音的第一反映")
    st.video("加纳.mp4")
    yi = st.radio('选择：',['A', 'B'],captions=['不管了，先加钠', '你妈了个'])
    if yi=="A":
        chengji+=10
    st.write("2.这首歌叫什么？")
    st.video("sos.mp4")
    er = st.radio('选择：',['A', 'B',"C","D"],captions=['Paradise', '独攀',"凌驾","SOS"])
    if er=="D":
        chengji+=10

    st.subheader("二、选择题（共2题，每题10分）")
    st.write("3.牛肉我不吃，____________")
    san = st.radio('选择：',['A', 'B',"C","D"],captions=['应为他菜', '荒野抛尸',"应为它善","诗人握持"])
    if san=="C":
        chengji+=10
    st.write("4.下列说法错误的是")
    si = st.radio('选择：',['A', 'B',"C","D"],captions=['俄罗斯大贝塔是三轮车', '咖啡不断加加加是林升干的',"蓝色妖姬切尔西是皮小浪演的","nice爷爷本名迈克尔·罗森"])
    if si=="A":
        chengji+=10
        
    st.subheader("三、填空题（共3题，每题10分）")
    wu=st.text_input("5.李云龙拿的是什么？")
    if wu=="意大利炮":
        chengji+=10
    liu=st.text_input("6.图中的配文是？")
    st.image("不是哥们.jpg")
    if liu=="不是哥们"or liu=="不是，哥们":
        chengji+=10
    qi=st.text_input("7.俄罗斯比例中普京的那只手不会动？")
    if qi=="右手":
        chengji+=10

    st.subheader("四、综合题（共3题，每题10分）")
    st.image("小丑.png")
    ba=st.text_input("8.此图的配文是？")
    if ba=="不听老人言，磕到甲沟炎":
        chengji+=10
    jiu=st.text_input("9.原视频的音乐叫什么？（不需要书名号，注意大小写和空格）")
    if jiu=="That girl":
        chengji+=10
    shi=st.text_input("与此图相似的梗是")
    if shi=="海公牛":
        chengji+=10

    if st.button("提交"):
        st.write("你的分数是",chengji,"分")

def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def img_fan(img):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][0]
            g=img_array[x,y][1]
            b=img_array[x,y][2]
            img_array[x,y]=(255-r,255-g,255-b)
    return img

#page=st.sidebar.radio("你是傻子吗？",['是','当然'])
page = st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智能词典","我的留言区","小游戏","网络梗考试"])

if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具' :
    page2()
elif page == '我的智能词典' :
    page3()
elif page == '我的留言区' :
    page4()
elif page=="小游戏":
    page5()
elif page=="网络梗考试":
    page6()