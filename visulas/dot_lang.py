import streamlit as st
import graphviz as gviz 

st.title('Grapghviz')
st.code('''st.graphviz_chart('digraph{
                  "Data" -> "testing data"
                  "Data" -> "training data"
                  "training data" -> "ML Algorithm"
                  "ML Algorithm" -> "Model"
                  "testing data" -> "Model"
                  "New data" -> "Model"
            }')          
''',language='python') 

st.graphviz_chart('''
            digraph{
                  "Data" -> "testing data"
                  "Data" -> "training data"
                  "training data" -> "ML Algorithm"
                  "ML Algorithm" -> "Model"
                  "testing data" -> "Model"
                  "New data" -> "Model"
            }          
''')
st.markdown("## another way for graphviz")

st.code('''graph = gviz.Digraph()
graph.edge('Data','testing data')
graph.edge('Data','training data')
graph.edge('training data','ML Algorithm')
graph.edge('ML Algorithm','Model')
graph.edge('testing data','Model')
graph.edge('New data','Model')
st.graphviz_chart(graph)
''',language='python'

)

graph = gviz.Digraph()
graph.edge('Data','testing data')
graph.edge('Data','training data')
graph.edge('training data','ML Algorithm')
graph.edge('ML Algorithm','Model')
graph.edge('testing data','Model')
graph.edge('New data','Model')
st.graphviz_chart(graph)

