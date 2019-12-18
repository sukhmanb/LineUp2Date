import React from 'react';
import axios from 'axios';
import Welcome from './Welcome.js'
import Team from './Team.js'


class Layout extends React.Component {
  constructor(props) {
    super(props);
    let storedsubmitted=false
    let storedemail=localStorage.getItem('email') || ''
    if (storedemail!='') {
      storedsubmitted=true
    }
    this.state = {email:storedemail,submitted:storedsubmitted,isFetchingData:false,data:null};
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handleSubmitChange = this.handleSubmitChange.bind(this);

    //
    // this.handleChange = this.handleChange.bind(this);
    // this.handleSubmit = this.handleSubmit.bind(this);
  }
  componentDidMount () {
    if (this.state.submitted==true) {
      console.log("Email is:")
      console.log(this.state.email)
      this.setState({ isFetchingData: true });
      axios.get('http://localhost:5000/home',{params:{'email':this.state.email}}).then((data) => {
        console.log(data)
        // This is how you access the data
        console.log(data.data[0]["team_name"])
        // console.log(type(data.data[0]))
        let count=0
        let theteam=[]
        for (const [ key, value ] of Object.entries(data.data[0])) {
          if (count<3) {
            //team_name, team_url, game_key
            theteam.push(<h3>value</h3>)
          }
          else {
            //roster
            let fullname=value.fullname;
            let selected_position=value.selected_position;
            let headshoturl=value.headshot.headshot.url;
            let headshotsize=value.headshot.headshot.size;
            theteam.push(<div><p>fullname</p><p>selected_position</p>)
            theteam.push(<img src={headshoturl.toString()} alt={fullname.toString()} />)
            theteam.push(</div>)
            // console.log(value.fullname)
            // console.log(value.selected_position)
            // console.log(value.headshot.headshot.url)
            // console.log(value.headshot.headshot.size)

          }
          count=count+1;
        }
        console.log(theteam)
        this.setState({
          isFetchingData: true,
          data:data
        });
      });
    }
  }

  handleEmailChange(childemail) {
    console.log(childemail)
    this.setState({email:childemail});
  }
  handleSubmitChange(childsubmit) {
    console.log(childsubmit)
    this.setState({submitted:childsubmit});
    localStorage.setItem('email', this.state.email);
  }
  render() {
    let codeblock=null
    if (!this.state.data) {
      codeblock=<p>No data</p>;
    }
    if (!this.state.isLoading) {
      codeblock=<p>Loading data</p>;
    }
    codeblock=<p>{this.state.data}</p>;
    // NEED TO SOMEHOW DISPLAY THE DATA
    return (
      <div>
      {this.state.submitted ? <div><h3>{this.state.email}</h3><Team data={this.state.data} /></div>:<Welcome email={this.state.email} onEmailChange={this.handleEmailChange} onSubmitChange={this.handleSubmitChange} />}
      </div>
    );
  }
}

export default Layout;
