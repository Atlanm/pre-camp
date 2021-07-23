    <style>
div.box {
    text-align: left;
  background-color: lightgrey;
  width: 500px;
  border: 10px midnightblue;
  padding: 50px;
  margin: 100px;
}

div.text{
    font-family: Nazanin,serif;
    text-align: right;
}
</style>
    <title>ÇáæÑíÊã KMP</title>

    <div class="text">
        <pre style="text-align: right">
        ÇáæÑíÊã ÊØÈíŞ KMP ÇÒ ÎÇÕíÊ ÊŞÓíã Çáæ (Çáæíí ˜å ÏÇÑÇí åãÇä Çáæí İÑÚí ÇÓÊ ˜å ÈíÔ ÇÒ í˜ ÈÇÑ ÏÑ Çáæ ÙÇåÑ ãí ÔæÏ) æ ÈåÈæÏ ÈÏÊÑíä ÍÇáÊ ÈÑÇí O (n) ÇÓÊİÇÏå ãí˜äÏ.
            ÇíÏå ÇÕáí ÏÑ ÔÊ ÇáæÑíÊã KMP Çíä ÇÓÊ ˜å: åÑ ÒãÇä ˜å ÚÏã ÊØÇÈŞ ÑÇ ÊÔÎíÕ ÏÇÏíã (ÈÚÏ ÇÒ äÏ ãæÑÏ ãäØÈŞ)¡ ÈÇ ÏÇäÓÊä ÈÑÎí ÇÒ ˜ÇÑÇ˜ÊÑåÇí ãÊä ˜å ÏÑ äÌÑå ÈÚÏí æÌæÏ ÏÇÑäÏ ÈÇ ÇÓÊİÇÏå ÇÒ Çíä ÇØáÇÚÇÊ ÇÒ ÇäÌÇã İÑÂíäÏí ÇäØÈÇŞ ÈÑÇí ˜ÇÑ˜ÊÑ åÇíí ˜å ÇÒ ÇäØÈÇŞ Âä åÇ ÇØãíäÇä ÏÇÑíã ÌáæíÑí ãí˜äíã.
        <b>äÍæå ÚãÇá˜ÑÏ ÇáæÑíÊã</b>
        </pre>
         <ul>
            <li>ÇÈÊÏÇ ÈÑÇí ÈÑÑÓí Çã ÒãÇäí ÈÑÇí ÇíÔ ãÊä ÇÍÊíÇÌ Èå íÔ ÑÏÇÒÔ Çáæ ÌÓÊÌæ ÈÑÇí íÇİÊä íÔæäÏ åÇ æ ÓæäÏ åÇ åÓÊíã ÊÇ äÍæå Ê˜ÑÇÑ ˜ÇÑ˜ÊÑ åÇ ÏÑ Çáæ ÑÇ ÏÑ í˜ áíÓÊ ĞÎíÑå ˜äíã</li>
            <li>ÓÓ ÈÇ ÊæÌå Èå Ê˜ÑÇÑ íÔæäÏ åÇ ÏÑ ÓæäÏ åÇ ÈÇ ÊæÌå Èå ÊØÇÈŞ ãÊä ÈÇ Çáæ æ áíÓÊ íÔ ÑÏÇÒÔ ÓÇÎÊå ÔÏå Çã åÇí ÌÓÊÌæ ÊÚííä ãí ÔæÏ.</li>
         </ul>
        <pre style="text-align: right">
         <b> ÚãáíÇÊ íÔ ÑÏÇÒÔ </b>
        ÈÑÇí ÊÚííä áíÓÊ íÔæäÏ åÇí ãäÇÓÈ ˜å ÏÑ ÓæäÏ åÇ(LPS) Ê˜ÑÇÑ ÔÏå ÇäÏ ÇÈÊÏÇ áÇÒã ÇÓÊ ˜å ÏÑ íãÇíÔ ÏÑ Çáæ ÇäÌÇã íÑÏ ˜å ÈØæÑ ãÚãæá ÏÑÇíå Çæá ÈÑÇí åãå Çáæ åÇ ÈÑÇÈÑ 0 ãí ÈÇÔÏ
            ÓÓ ÈÇ ãŞÇíÓå åÑ ˜ÇÑ˜ÊÑ ÈÇ ÇÈÊÏÇí áíÓÊ ÏÑ ÕæÑÊ Ê˜ÑÇÑ íÔæäÏ ÏÑ ÓæäÏ ãŞÏÇÑ 1 ÑÇ Èå Âä ÏÑÇíå ÇÒ áíÓÊ ÊÇ ÌÇíí ˜å Ê˜ÑÇÑ Çáæí íÔæäÏí ÇÏÇãå ÏÇÑÏ ÇÖÇİå ãí ˜äíã æ ÇÑ ˜ÇÑ˜ÊÑ ãÊİÇæÊ ÙÇåÑ ÔÏ ãŞÏÇÑ 1 ÑÇ ÇÒ Âä ˜ã ãí ˜äíã ÊÇ íãÇíÔ Çáæ Èå ÇäÊåÇ ÈÑÓÏ. ÈÑÇí İåã ÈåÊÑ Ô˜á ÒíÑ ÑÇ ãÔÇåÏ ˜äíÏ:
        <img src="https://miro.medium.com/max/700/1*OIb4erqMedwaze8aTUi9gw.gif" alt="LPS">
            åãäíä ãËÇá ÒíÑ ÈÑÇí ãÍÇÓÈå íÔ ÑÏÇÒÔ Çáæ äÔÇä ÏÇÏå ÔÏå ÇÓÊ:
            </pre>
    </div>

    <div class="box">
            <pre>pat[] = "<strong>AAACAAAA</strong>"

    len = 0, i  = 0.
    <strong>lps[0] is always 0</strong>, we move
    to i = 1

    len = 0, i  = 1.
    Since pat[len] and pat[i] match, do len++,
    store it in lps[i] and do i++.
    len = 1, <strong>lps[1] = 1</strong>, i = 2

    len = 1, i  = 2.
    Since pat[len] and pat[i] match, do len++,
    store it in lps[i] and do i++.
    len = 2, <strong>lps[2] = 2</strong>, i = 3

    len = 2, i  = 3.
    Since pat[len] and pat[i] do not match, and len &gt; 0,
    set len = lps[len-1] = lps[1] = 1

    len = 1, i  = 3.
    Since pat[len] and pat[i] do not match and len &gt; 0,
    len = lps[len-1] = lps[0] = 0

    len = 0, i  = 3.
    Since pat[len] and pat[i] do not match and len = 0,
    Set <strong>lps[3] = 0</strong> and i = 4.
    We know that characters pat
    len = 0, i  = 4.
    Since pat[len] and pat[i] match, do len++,
    store it in lps[i] and do i++.
    len = 1, <strong>lps[4] = 1</strong>, i = 5

    len = 1, i  = 5.
    Since pat[len] and pat[i] match, do len++,
    store it in lps[i] and do i++.
    len = 2, <strong>lps[5] = 2</strong>, i = 6

    len = 2, i  = 6.
    Since pat[len] and pat[i] match, do len++,
    store it in lps[i] and do i++.
    len = 3, <strong>lps[6] = 3</strong>, i = 7

    len = 3, i  = 7.
    Since pat[len] and pat[i] do not match and len &gt; 0,
    set len = lps[len-1] = lps[2] = 2

    len = 2, i  = 7.
    Since pat[len] and pat[i] match, do len++,
    store it in lps[i] and do i++.
    len = 3, <strong>lps[7] = 3</strong>, i = 8

    We stop here as we have constructed the whole lps[].
        </pre>
    </div>

    <div class="text">
        <pre style="text-align: right">
            <b>ÚãáíÇÊ ÌÓÊÌæ</b>
        ÏÑ Çíä ÈÎÔ ãÇääÏ ÇáæÑíÊã naive ÇÈÊÏÇ ÊØÇÈŞ Çáæ æ ãÊä ÑÇ ÈÑÑÓí ãí ˜äíã æ ÏÑÕæÑÊí ˜å Èå ÚÏã ÊØÇÈŞ ÈÑÓíã ÏÑÇíå ˜ÇÑ˜ÊÑí ÇÒ Çáæ ˜å Èå ÚÏã ÊØÇÈŞ ÑÓíÏå ÇÓÊ ÑÇ ãÓÇæí ÈÇ Çã ãÊäÇÙÑ åãÇä ÏÑÇíå-1 ÈÑÇÈÑ ÑİÊå æ ÏæÈÇÑå ÚãáíÇÊ ÌÓÊÌæ ÑÇ ÇÒ ÓÑ ãí íÑíã ÊÇ äåÇíÊÇ Èå ÇäÊåÇí ãÊä ÈÑÓíã. Çíä ˜ÇÑ ÈÇÚË ˜ÇåÔ íãÇíÔ ÏÑ ãÊä ÈÑÇí Çáæ åÇíí ˜å íÔæäÏ æ ÓæäÏ åÇí ãÔÇÈå ÏÇÑäÏ ãí ÔæÏ. Ô˜á ÒíÑ äÔÇä ÏåäÏå Úãá˜ÑÏ Çíä ÇáæÑíÊã ÈÇ ÇÓÊİÇÏå ÇÒ áíÓÊ LPS ãí ÈÇÔÏ.

             <img src="https://miro.medium.com/max/700/1*hGaxEHtNvfYJDxHeFV171g.png" alt="KMP">
             <img src="https://miro.medium.com/max/700/1*kPepYjAnJqlP495bjI0p8w.png" alt="KMP">

            ÏÑ ãËÇá ÒíÑ äíÒ äÍæå Úãá˜ÑÏ Çíä ÇáæÑíÊã äÔÇä ÏÇÏå ÔÏå ÇÓÊ:
        </pre>
    </div>

    <div class="box">
    <pre>txt[] = "<strong>AAAA</strong>ABAAABA"
    pat[] = "<strong>AAAA</strong>"
    lps[] = {0, 1, 2, 3}

    i = 0, j = 0
    txt[] = "<strong><span style="color: Red; ">A</span>AAA</strong>ABAAABA"
    pat[] = "<strong><font color="Red">A</font>AAA</strong>"
    txt[i] and pat[j] match, do i++, j++

    i = 1, j = 1
    txt[] = "<strong>A<font color="Red">A</font>AA</strong>ABAAABA"
    pat[] = "<strong>A<font color="Red">A</font>AA</strong>"
    txt[i] and pat[j] match, do i++, j++

    i = 2, j = 2
    txt[] = "<strong>AA<font color="Red">A</font>A</strong>ABAAABA"
    pat[] = "<strong>AA<font color="Red">A</font>A</strong>"
    pat[i] and pat[j] match, do i++, j++

    i = 3, j = 3
    txt[] = "<strong>AAA<font color="Red">A</font></strong>ABAAABA"
    pat[] = "<strong>AAA<font color="Red">A</font></strong>"
    txt[i] and pat[j] match, do i++, j++

    i = 4, j = 4
    Since j == M, print <strong>pattern found</strong> and reset j,
    j = lps[j-1] = lps[3] = 3

    Here unlike Naive algorithm, we do not match first three
    characters of this window. Value of lps[j-1] (in above
    step) gave us index of next character to match.
    i = 4, j = 3
    txt[] = "A<strong>AAA<font color="Red">A</font></strong>BAAABA"
    pat[] =  "<strong>AAA<font color="Red">A</font></strong>"
    txt[i] and pat[j] match, do i++, j++

    i = 5, j = 4
    Since j == M, print <strong>pattern found</strong> and reset j,
    j = lps[j-1] = lps[3] = 3

    Again unlike Naive algorithm, we do not match first three
    characters of this window. Value of lps[j-1] (in above
    step) gave us index of next character to match.
    i = 5, j = 3
    txt[] = "AA<strong>AAA<font color="Red">B</font></strong>AAABA"
    pat[] =   "<strong>AAA<font color="Red">A</font></strong>"
    txt[i] and pat[j] do NOT match and j &gt; 0, change only j
    j = lps[j-1] = lps[2] = 2

    i = 5, j = 2
    txt[] = "AAA<strong>AA<font color="Red">B</font>A</strong>AABA"
    pat[] =    "<strong>AA<font color="Red">A</font>A</strong>"
    txt[i] and pat[j] do NOT match and j &gt; 0, change only j
    j = lps[j-1] = lps[1] = 1

    i = 5, j = 1
    txt[] = "AAAA<strong>A<font color="Red">B</font>AA</strong>ABA"
    pat[] =     "<strong>A<font color="Red">A</font>AA</strong>"
    txt[i] and pat[j] do NOT match and j &gt; 0, change only j
    j = lps[j-1] = lps[0] = 0

    i = 5, j = 0
    txt[] = "AAAAA<strong><font color="Red">B</font>AAA</strong>BA"
    pat[] =      "<strong><font color="Red">A</font>AAA</strong>"
    txt[i] and pat[j] do NOT match and j is 0, we do i++.

    i = 6, j = 0
    txt[] = "AAAAAB<strong><font color="Red">A</font>AABA</strong>"
    pat[] =       "<strong><font color="Red">A</font>AAA</strong>"
    txt[i] and pat[j] match, do i++ and j++

    i = 7, j = 1
    txt[] = "AAAAAB<strong>A<font color="Red">A</font>AB</strong>A"
    pat[] =       "<strong>A<font color="Red">A</font>AA</strong>"
    txt[i] and pat[j] match, do i++ and j++

    We continue this way...
        </pre>
    </div>

    <div class="text">
        <pre style="text-align: right;">
            <b>ííÏí ãÍÇÓÈÇÊí</b>
        Çíä ÇáæÑíÊã ííÏí ãÍÇÓÈÇÊí ÑÇ ÈÑÇí ÈÏÊÑíä ÍÇáÊ ÇáæÑíÊã Naive ÑÇ ÊÇ O(m+n) ˜ÇåÔ ãí ÏåÏ æ ÈÇÚË ˜ÇåÔ ãÍÇÓÈÇÊ æ ÇäÌÇã ãÍÇÓÈÇÊ Ê˜ÑÇÑí ãíÔæÏ.
        <b>:ãÒÇíÇ</b>
        </pre>
        <ul style="text-align: right">
            <li>ÈåÈæÏ ÇÓÊİÇÏå ÇÒ ÒãÇä ÑÏÇÒÔ æ ÍÇİÙå ÏÑ Çáæ åÇíí ˜å ÔÇãá ˜ÇÑ˜ÊÑ åÇí Ê˜ÑÇÑí ãí ÈÇÔäÏ</li>
        </ul>
            <p style="text-align: right"><b>:ãÚÇíÈ</b></p>
        <ul style="text-align: right">
            <li>ÇİÒÇíÔ ãÍÇÓÈÇÊ ÈÏáíá æÌæÏ íÔ ÑÏÇÒÔ ÏÑ Çáæ åÇíí ˜å ˜ÇÑ˜ÊÑ åÇí ãÔÇÈå äÏÇÑäÏ.</li>
        </ul>
    </div>
</head>