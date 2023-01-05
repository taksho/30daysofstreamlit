import streamlit as st

st.header('st.latex')

st.text('無限等比級数')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
''')

st.caption('LaTex での記述内容')
latex = '''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = 
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)'''

st.code(latex, language='latex')


st.text('オイラーの公式')

st.latex(r'''e^{iax}=\cos(ax)+i\sin(ax)''')

st.caption('LaTex での記述内容')
latex = '''e^{iax}=\cos(ax)+i\sin(ax)'''
st.code(latex, language='latex')
