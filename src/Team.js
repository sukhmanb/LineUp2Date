import React from 'react';
import styled from 'styled-components';
// import Nav from 'react-bootstrap/Navbar';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav'
import NavDropdown from 'react-bootstrap/NavDropdown'

// import NavDropdown from 'react-bootstrap/Navbar';


const Div = styled.div `
background-color: #D0D0D0;
color: black;
width:855px;
height:70px;
margin:0 auto;
margin-bottom:20px;
text-align:left;
border-radius: 25px;
`;
// const Logo = styled.img `
// float:left;
// height:100px;
// width:200px;
// `
const styleImg={'margin-left':'10px','line-height':'70px'}
const styleSpanone={'margin-left': '20px','line-height': '70px','font-weight':'bold'};
const styleSpantwo={'float': 'right','line-height': '70px','font-weight':'bold'};
const h3centered={'text-align':'center','font-weight':'bold','margin-bottom':'2px'};


// const Playername = styled.p ``
class Team extends React.Component {
// this.props.team
// First three key value pairs are team_name, team_url,game_key
// After this, it is the roster of the team: QB,WR1,WR2,RB1,RB2,TE,W/R/T,
constructor(props) {
  super(props);
  console.log("PRINTING THE PROPS:")
  console.log(this.props)
  this.state = {displayedTeam:0};
  this.handleClick=this.handleClick.bind(this)

}
handleClick(event) {
  let dataid=event.target.getAttribute('data-teamid');
  // CONSOLE.LOG IS CORRECT BUT THEN SOMEHOW WHEN YOU SET STATE dataid is undefinedd
  console.log(dataid);
  this.setState({displayedTeam:dataid})
  console.log("Handle click, the data id is:")

  // this.setState({displayedTeam:e.target.getAttribute('teamid')})
}
constructNavbar() {
  console.log("THIS IS WHERE WE CONSTRUCT THE NAVBAR")
  let teamname=this.props.data.data[this.state.displayedTeam].team_name;
  let leaguename=this.props.data.data[this.state.displayedTeam].game_key;

  console.log(teamname)
  let navbarlist=[];
  // navbarlist.push(<div><Navbar bg="light" variant="light"><Navbar.Brand href="#home"><img src="design/nfl100.png" width="100" height="50" className="d-inline-block align-top" alt="React Bootstrap logo"/></Navbar.Brand><Navbar.Toggle aria-controls="basic-navbar-nav" /><Navbar.Collapse id="basic-navbar-nav"><Nav className="mr-auto"><NavDropdown title={teamname} id="basic-nav-dropdown">)
  // navbarlist.push(<Navbar bg="light" variant="light"><Navbar.Brand href="#home"><img src="design/nfl100.png" width="100" height="50" className="d-inline-block align-top" alt="React Bootstrap logo"/></Navbar.Brand><Navbar.Toggle aria-controls="basic-navbar-nav" /><Navbar.Collapse id="basic-navbar-nav"><Nav className="mr-auto"><NavDropdown title={this.props.data.data[this.state.displayedTeam].team_name} id="basic-nav-dropdown">)
  // navbarlist.push(<NavDropdown title={this.props.data.data[this.state.displayedTeam].team_name} id="basic-nav-dropdown">)
  console.log(navbarlist)
  let numteams=this.props.data.data.length;
  var i=0;
  for (i=0; i < this.props.data.data.length; i++) {
    if (i==this.state.displayedTeam) {
      console.log("Displayed team is:")
      console.log(i)

    }
    else {
      console.log("Ids are:")
      console.log(i)
      // console.log("blah")
      navbarlist.push(<NavDropdown.Item data-teamid={i} onClick={this.handleClick}>{this.props.data.data[i].team_name}<i className="fas fa-basketball-ball"></i></NavDropdown.Item>);

    }
  }
  // navbarlist.unshift(<NavDropdown title={teamname} id="basic-nav-dropdown">);
  let navbarlist2=[];
  navbarlist2.push(<NavDropdown title={teamname} id="basic-nav-dropdown">{navbarlist}</NavDropdown>);
  let navbarlist3=[];

  // navbarlist.push(</NavDropdown>);
  navbarlist3.push(<Nav className="mr-auto">{navbarlist2}</Nav>);
  // navbarlist.push(</Nav>);
  let navbarlist4=[];
  navbarlist4.push(<Navbar.Collapse id="basic-navbar-nav">{navbarlist3}</Navbar.Collapse>);
  // navbarlist.push(</Navbar.Collapse>);
  let imgsrc="design/"+leaguename+".png";
  let navbarlist5=[];
  navbarlist5.push(<Navbar><Navbar.Brand href="#home"><img src={imgsrc} width="100" height="50" className="d-inline-block align-top" alt="React Bootstrap logo"/></Navbar.Brand><Navbar.Toggle aria-controls="basic-navbar-nav" />{navbarlist4}</Navbar>);
  // navbarlist.push(</Navbar>);
  // navbarlist.unshift(<div>);
  // navbarlist.push(</div>);
  return navbarlist5


  // navbarlist.push(</NavDropdown></Nav></Navbar.Collapse></Navbar>)
  // return navbarlist

}
constructRoster(team) {
  let count=0
  let theteam=[]
  //
  let numteams=this.props.data.data.length;
  console.log(numteams)
  for (const [ key, value ] of Object.entries(this.props.data.data[team])) {
    if (count<3) {
      //team_name, team_url, game_key
      if (count==0)
      {
        theteam.push(<h3 style={h3centered}>{value}</h3>)
      }
      // team_url
      if (count==1)
      {
        theteam.push(<div style={h3centered}><a target="_blank" href={value}><img src="design/yahoo.png" width="50" height="50" /></a></div>)
      }
      //game_key
      if (count==2) {
        console.log(value)

      }
    }
    else {
      //roster
      let fullname=value.fullname;
      this.fullname=value.fullname;
      let selected_position=value.selected_position;
      let headshoturl=value.headshot.headshot.url;
      let headshotsize=value.headshot.headshot.size;
      theteam.push(<Div><img style={styleImg} src={headshoturl.toString()} alt={fullname.toString()} /><span style={styleSpanone}>{fullname}</span><span style={styleSpantwo}>{selected_position}</span></Div>)
      // console.log(value.fullname)
      // console.log(value.selected_position)
      // console.log(value.headshot.headshot.url)
      // console.log(value.headshot.headshot.size)

    }
    count=count+1;
  }
  console.log(theteam)
  return theteam
}

  // createTable = () => {
  //   let table = []
  //
  //   // Outer loop to create parent
  //   for (let i = 0; i < 3; i++) {
  //     let children = []
  //     //Inner loop to create children
  //     for (let j = 0; j < 5; j++) {
  //       children.push(<td>{`Column ${j + 1}`}</td>)
  //     }
  //     //Create the parent and add the children
  //     table.push(<tr>{children}</tr>)
  //   }
  //   return table
  // }


  render() {
    return(
      <div>
        {this.constructNavbar()}
        {this.constructRoster(this.state.displayedTeam)}
      </div>
    )
  }

}
export default Team;
