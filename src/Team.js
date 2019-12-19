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


// const Playername = styled.p ``
class Team extends React.Component {
// this.props.team
// First three key value pairs are team_name, team_url,game_key
// After this, it is the roster of the team: QB,WR1,WR2,RB1,RB2,TE,W/R/T,
constructor(props) {
  super(props);
  console.log("PRINTING THE PROPS:")
  console.log(this.props)
}
constructRoster() {
  let count=0
  let theteam=[]
  for (const [ key, value ] of Object.entries(this.props.data.data[2])) {
    if (count<3) {
      //team_name, team_url, game_key
      theteam.push(<h3>{value}</h3>)
    }
    else {
      //roster
      let fullname=value.fullname;
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
      <Navbar bg="dark" variant="dark">
      <Navbar.Brand href="#home">
      <img
      src="design/nfl100.png"
      width="100"
      height="50"
      className="d-inline-block align-top"
      alt="React Bootstrap logo"
      />
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
<Navbar.Collapse id="basic-navbar-nav">
  <Nav className="mr-auto">
    <NavDropdown title="Dropdown" id="basic-nav-dropdown">
      <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
      <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
      <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
      <NavDropdown.Divider />
      <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
    </NavDropdown>
  </Nav>
  </Navbar.Collapse>
      </Navbar>
        {this.constructRoster()}
      </div>
    )
  }

}
export default Team;
