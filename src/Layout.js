import React from 'react';
import axios from 'axios';
import Welcome from './Welcome.js'
import Team from './Team.js'

const h3centered={'textAlign':'center','fontWeight':'bold','margin-bottom':'2px'};


class Layout extends React.Component {
  constructor(props) {
    super(props);
    let storedsubmitted=false
    let storedemail=localStorage.getItem('email') || ''
    if (storedemail!='') {
      console.log("We have email in localstorage")
      storedsubmitted=true
    }
    this.state = {email:storedemail,submitted:storedsubmitted,isFetchingData:false,data:null,authurl:null};
    this.handleEmailChange = this.handleEmailChange.bind(this);
    this.handleSubmitChange = this.handleSubmitChange.bind(this);
    this.handleAuthResponse = this.handleAuthResponse.bind(this);

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
        // let count=0
        // let theteam=[]
        // for (const [ key, value ] of Object.entries(data.data[0])) {
        //   if (count<3) {
        //     //team_name, team_url, game_key
        //     theteam.push(<h3>value</h3>)
        //   }
        //   else {
        //     //roster
        //     let fullname=value.fullname;
        //     let selected_position=value.selected_position;
        //     let headshoturl=value.headshot.headshot.url;
        //     let headshotsize=value.headshot.headshot.size;
        //     theteam.push(<div><p>fullname</p><p>selected_position</p>)
        //     theteam.push(<img src={headshoturl.toString()} alt={fullname.toString()} />)
        //     theteam.push(</div>)
        //     // console.log(value.fullname)
        //     // console.log(value.selected_position)
        //     // console.log(value.headshot.headshot.url)
        //     // console.log(value.headshot.headshot.size)
        //
        //   }
        //   count=count+1;
        // }
        // console.log(theteam)
        this.setState({
          isFetchingData: false,
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
  handleAuthResponse(authurl) {
    console.log("In the Layout handleresponse function:")
    console.log(authurl)
    console.log(authurl["data"]["auth_url"])
    this.setState({authurl:authurl["data"]["auth_url"]});

  }
  render() {
    let codeblock=null
    if (this.state.submitted) {
      if (this.state.authurl==null) {
        //user already signed up and has completed the authorization process. Now the data needs to be retrieved.
        if (this.state.data==null) {
          //Data is either being fetched or error?
          if (this.state.isFetchingData) {
            codeblock=<div><img className="App-logo" src="lineup2Date.png"/><h3>{this.state.email}</h3><p>Fetching data</p><i className="fa fa-spinner fa-spin"></i></div>;
          }
          else {
            codeblock=<div><img className="App-logo" src="lineup2Date.png"/><h3>{this.state.email}</h3><i className="fa fa-spinner fa-spin"></i></div>;
          }
        }
        else {
          //Data has been retrieved
            codeblock=<div className="App-left"><Team data={this.state.data} /></div>

        }
      }
      else {
        //user just submitted the signup form and now we need to get the user authorized from yahoo. this.state.authurl contains the yahoo auth url. Insert a button to the authorization url
        codeblock=<div><img className="App-logo" src="lineup2Date.png"/><h3>{this.state.email}</h3><p>This app requires authorization from Yahoo to access your information and roster. Please click the button below to give access.</p><i className="fa fa-spinner fa-spin"></i><div style={h3centered}><a target="_blank" href={this.state.authurl}><img src="design/yahoo.png" width="50" height="50" /></a></div></div>;
      }

    }
    else {
      //user signing up for the first time
      codeblock=<Welcome email={this.state.email} onEmailChange={this.handleEmailChange} onSubmitChange={this.handleSubmitChange} onAuthResponse={this.handleAuthResponse}/>
    }
    return (
      <div>
      {codeblock}
      </div>
    );
    // if (this.state.data==null) {
    //   if (this.state.isFetchingData==false) {
    //     codeblock=<div><img className="App-logo" src="lineup2Date.png"/><h3>{this.state.email}</h3><p>Completing signup process, authorize app with Yahoo. Once you authorize the app, this page will automatically refresh.</p><i className="fa fa-spinner fa-spin"></i><p>{this.state.authurl}</p></div>;
    //     // setTimeout(function() {
    //     //   window.location.reload();}, 30000);
    //   }
    //   else {
    //     codeblock=<div><img className="App-logo" src="lineup2Date.png"/><h3>{this.state.email}</h3><p>Fetching data</p><i className="fa fa-spinner fa-spin"></i></div>;
    //   }
    // }
    // else {
    //   codeblock=<div className="App-left"><Team data={this.state.data} /></div>
    // }
    // // NEED TO SOMEHOW DISPLAY THE DATA
    // return (
    //   <div>
    //   {this.state.submitted ? <div>{codeblock}</div>:<Welcome email={this.state.email} onEmailChange={this.handleEmailChange} onSubmitChange={this.handleSubmitChange} onAuthResponse={this.handleAuthResponse}/>}
    //   </div>
    // );
  }
}

export default Layout;
