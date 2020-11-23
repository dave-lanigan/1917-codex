import React, {Component} from 'react';

export default function Header(props){
    let title = props.title;
    console.log("inside header")
    console.log(title)
    let title_formatted=title;
    let t = title.slice( 0, title.indexOf("-"))

    title_formatted = title_formatted.replace("-"," ")
    title_formatted = title_formatted.replace("_"," ")
    title_formatted = title_formatted.replace(/(^[a-z])|(\s+[a-z])/g, txt => txt.toUpperCase());
    
//    return(<h1>TITLE</h1>);
    if (t=="book"){ return(<h1 id={title} ><u>{title_formatted}</u></h1>);}
    else if (t=="part"){ return(<h2 id={title}>{title_formatted}</h2>);}
    else if (t=="section"){ return(<h3 id={title}>{title_formatted}</h3>);}
    else if (t=="title"){ return(<h4 id={title}>{title_formatted}</h4>);}
    else if (t=="chapter"){ return(<h5 id={title}>{title_formatted}</h5>);}
    else if (t=="article"){ return(<h6 id={title}>{title_formatted}</h6>);}
}
 
function Canon(props){
    let title = props.title;
    let content=props.content;
    
    return(<p><b>{title}</b> {content}</p>);

}

export {Header,Canon};