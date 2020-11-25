import React, {Component, useState, useEffect} from 'react';
import ReactDOM from 'react-dom';
//import {Header,Canon} from 'chapters';
import {Header,Canon} from './chapters';
import InfiniteScroll from 'react-infinite-scroll-component';

export default function App(props) {
  
  const [dataInfo, setData] = useState({loading:true, data: null});


  function ggetData() {
      
    let url="http://127.0.0.1:8000/api/v0/codex/book-1/";

    return fetch( url ).then( (resp) => resp.json()).then( (json) =>{
        setData( {loading: false, data: json } )
    }).catch( (error) => console.log(error) )   
}

  function formatData(d){
    let out=[];

    let key_stack=Object.keys(d)
    let dict_stack = [d]
    while(key_stack.length!=0){
    
      let key=key_stack.shift()
  
      d=dict_stack[0][key]
      if(typeof(d)=="string"){ 
        let title = key.replace("-"," ")
        title = title.replace(/(^[a-z])|(\s+[a-z])/g, txt => txt.toUpperCase());
        out.push( <Canon title={title} content={d}/> )
       }
       if (typeof(d)=="object") {
          out.push( <Header title={key}/> )
          dict_stack.unshift( d )
  
          let ks = Object.keys(d)
          for(let i=0;i<ks.length;i++){
            key_stack.unshift( ks[ ks.length - i - 1 ] )
          }
        }
        if ( key==Object.keys( dict_stack[0] ).pop() ){ dict_stack.shift() }
        if (d==undefined){
          let nothing=dict_stack.shift()
          key_stack.unshift( key )
        
          }
        }
    
    return out;

  }

  // function App() {
  //   useEffect(() => {
  //     ggetData();
  //   }, []);
  // }
   
  if (dataInfo.loading==true){  
    ggetData();
    return(<div className="loader center">Loading...</div>);}
  
  else if (dataInfo.loading==false){  
  
    
    let out = formatData(dataInfo.data)

    return(<div className="content-inner">{out.map( el => el )}</div>);
    
    // return(
    //   <div id="scrollableDiv">
    //   <InfiniteScroll
    //   dataLength={out.length}
    //   next={this.fetchMoreData}
    //   hasMore={true}
    //   loader={<h4>Loading...</h4>}
    //   scrollableTarget="scrollableDiv">
    //   <div className="content-inner">{out.map( el => el )}</div>
    //   </InfiniteScroll>
    //   </div>
    //     );
    }
  }

ReactDOM.render( <App />,document.getElementById('app') )