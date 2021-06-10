import React from 'react'
import ReactDOM from 'react-dom'

import App from './App.jsx'


class Doc extends React.Component{
    setPgTitle(pgtitle){
      document.title = pgtitle;
    }
  
    render(){
      return(
        <App pgTitle={this.setPgTitle}></App>
      )
    }
  }



ReactDOM.render(
    <Doc />,
    document.getElementById('root')
)