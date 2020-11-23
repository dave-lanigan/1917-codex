import React, {Component} from 'react';

export default function Header(props){
    let title = props.title;
    let title_formatted=title;

    title = title.slice( 0, title.indexOf("-"))

    title_formatted = title_formatted.replace("-"," ")
    title_formatted = title_formatted.replace("_"," ")
    title_formatted = title_formatted.replace(/(^[a-z])|(\s+[a-z])/g, txt => txt.toUpperCase());
    
//    return(<h1>TITLE</h1>);
    if (title=="book"){ return(<h1>{title_formatted}</h1>);}
    else if (title=="part"){ return(<h2>{title_formatted}</h2>);}
    else if (title=="section"){ return(<h3>{title_formatted}</h3>);}
    else if (title=="title"){ return(<h4>{title_formatted}</h4>);}
    else if (title=="chapter"){ return(<h5>{title_formatted}</h5>);}
    else if (title=="article"){ return(<h5>{title_formatted}</h5>);}
}
 
function Canon(props){
    let title = props.title;
    let content=props.content;
    
    return(<p><b>{title}</b> {content}</p>);

}

export {Header,Canon};