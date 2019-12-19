import React from 'react';

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
  for (const [ key, value ] of Object.entries(this.props.data.data[0])) {
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
      theteam.push(<div><p>{fullname}</p><p>{selected_position}</p><img src={headshoturl.toString()} alt={fullname.toString()} /></div>)
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
        {this.constructRoster()}
      </div>
    )
  }

}
export default Team;
