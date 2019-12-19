import React from 'react';
import styled from 'styled-components';

const Div = styled.div `
background-color: #D0D0D0;
color: black;
width:855px;
margin:0 auto;
margin-bottom:10px;
text-align:left;
`;
const Logo = styled.img `
float:left;
height:100px;
width:200px;
`
const styleSpanone={'margin-left': '20px','font-weight':'bold'};
const styleSpantwo={'float': 'right','font-weight':'bold'};


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
      theteam.push(<Div><img src={headshoturl.toString()} alt={fullname.toString()} /><span style={styleSpanone}>{fullname}</span><span style={styleSpantwo}>{selected_position}</span></Div>)
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
      <Logo src='design/nfl100.png' alt="nfl100" />
        {this.constructRoster()}
      </div>
    )
  }

}
export default Team;
