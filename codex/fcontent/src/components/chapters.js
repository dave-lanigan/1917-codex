import React, {Component} from 'react';

export default function Header(props){
    let title = props.title;
    let title_formatted=title;
    let t = title.slice( 0, title.indexOf("-"))

    title_formatted = title_formatted.replaceAll("-"," ")
    title_formatted = title_formatted.replace("_",": ")
    title_formatted = title_formatted.replace(/(^[a-z])|(\s+[a-z])/g, txt => txt.toUpperCase());
    
//    return(<h1>TITLE</h1>);
    if (t=="book"){ return(<h1 className="headings" id={title}><u>{title_formatted}</u></h1>);}
    else if (t=="part"){ return(<h2 className="headings" id={title}><u>{title_formatted}</u></h2>);}
    else if (t=="section"){ return(<h3 className="headings" id={title}><u>{title_formatted}</u></h3>);}
    else if (t=="title"){ return(<h4 className="headings" id={title}><u>{title_formatted}</u></h4>);}
    else if (t=="chapter"){ return(<h5 className="headings" id={title}><u>{title_formatted}</u></h5>);}
    else if (t=="article"){ return(<h6 className="headings" id={title}><u>{title_formatted}</u></h6>);}
}
 
function Canon(props){
    let title = props.title;
    let content=props.content;
    
    return(<p className="canon"><b>{title}:</b> {content}</p>);
}

export {Header,Canon};