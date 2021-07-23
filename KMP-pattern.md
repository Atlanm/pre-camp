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
    <title>������� KMP</title>

    <div class="text">
        <pre style="text-align: right">
        ������� ����� KMP �� ����� ����� ��� (����� �� ����� ���� ���� ���� ��� �� ��� �� � ��� �� ��� ���� �� ���) � ����� ������ ���� ���� O (n) ������� ����.
            ���� ���� �� ��� ������� KMP ��� ��� ��: �� ���� �� ��� ����� �� ����� ����� (��� �� ��� ���� �����)� �� ������ ���� �� ���ǘ����� ��� �� �� ����� ���� ���� ����� �� ������� �� ��� ������� �� ����� ������� ������ ���� ��ј�� ���� �� �� ������ �� �� ������� ����� ������ �����.
        <b>���� ������ �������</b>
        </pre>
         <ul>
            <li>����� ���� ����� ��� ����� ���� ���� ��� ������ �� ��� ������ ��� ����� ���� ����� ������ �� � ����� �� ����� �� ���� ʘ��� ��ј�� �� �� ��� �� �� � ���� ����� ����</li>
            <li>Ӂ� �� ���� �� ʘ��� ������ �� �� ����� �� �� ���� �� ����� ��� �� ��� � ���� ��� ������ ����� ��� ��� ��� ����� ����� �� ���.</li>
         </ul>
        <pre style="text-align: right">
         <b> ������ ��� ������ </b>
        ���� ����� ���� ������ ��� ����� �� �� ����� ��(LPS) ʘ��� ��� ��� ����� ���� ��� �� �� ������ �� ��� ����� ���� �� ���� ����� ����� ��� ���� ��� ��� �� ����� 0 �� ����
            Ӂ� �� ������ �� ��ј�� �� ������ ���� �� ���� ʘ��� ������ �� ����� ����� 1 �� �� �� ����� �� ���� �� ���� �� ʘ��� ���� ������� ����� ���� ����� �� ���� � ǐ� ��ј�� ������ ���� �� ����� 1 �� �� �� �� �� ���� �� ������ ��� �� ����� ����. ���� ��� ���� Ԙ� ��� �� ����� ����:
        <img src="https://miro.medium.com/max/700/1*OIb4erqMedwaze8aTUi9gw.gif" alt="LPS">
            ����� ���� ��� ���� ������ ��� ������ ��� ���� ���� ��� ���:
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
            <b>������ �����</b>
        �� ��� ��� ����� ������� naive ����� ����� ��� � ��� �� ����� �� ���� � ������� �� �� ��� ����� ����� ����� ��ј��� �� ��� �� �� ��� ����� ����� ��� �� ����� �� ��� ������ ���� �����-1 ����� ����� � ������ ������ ����� �� �� �� �� ����� �� ������ �� ������ ��� �����. ��� ��� ���� ���� ������ �� ��� ���� ��� ���� �� ������ � ����� ��� ����� ����� �� ���. Ԙ� ��� ���� ����� ����� ��� ������� �� ������� �� ���� LPS �� ����.

             <img src="https://miro.medium.com/max/700/1*hGaxEHtNvfYJDxHeFV171g.png" alt="KMP">
             <img src="https://miro.medium.com/max/700/1*kPepYjAnJqlP495bjI0p8w.png" alt="KMP">

            �� ���� ��� ��� ���� ����� ��� ������� ���� ���� ��� ���:
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
            <b>���ϐ� ��������</b>
        ��� ������� ���ϐ� �������� �� ���� ������ ���� ������� Naive �� �� O(m+n) ���� �� ��� � ���� ���� ������� � ����� ������� ʘ���� �����.
        <b>:�����</b>
        </pre>
        <ul style="text-align: right">
            <li>����� ������� �� ���� ������ � ����� �� ��� ���� �� ���� ��ј�� ��� ʘ���� �� �����</li>
        </ul>
            <p style="text-align: right"><b>:�����</b></p>
        <ul style="text-align: right">
            <li>������ ������� ����� ���� ��� ������ �� ��� ���� �� ��ј�� ��� ����� ������.</li>
        </ul>
    </div>
</head>