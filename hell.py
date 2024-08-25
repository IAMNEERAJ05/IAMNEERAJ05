import streamlit as st 
st.title("Edo okati,bro!!!")
st.header("""it's hell, guys!!!""")
st.subheader("This is sub-header")
st.caption("something something")
st.text("peace \n people!!")
st.markdown("***jazz day fest***")
st.markdown("### jazz day fest")
st.markdown("## jazz day fest")
st.markdown("# jazz day fest")
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.subheader("""Java Code""")
st.code("""public class GFG {
public static void main(String args[])
{
System.out.println("Hello World");
}
}""", language='java')
st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try {
adddlert("Welcome guest!");
}
catch(err) {
document.getElementById("demo").innerHTML = err.message;
}
</script> """)