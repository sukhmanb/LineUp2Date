import React from 'react';
import axios from 'axios';
// import Layout from './Layout.js'


class Welcome extends React.Component {
  constructor(props) {
    super(props);
    console.log(this.props)
    // console.log(this.props.email)
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    // this.props.onEmailChange = this.props.onEmailChange.bind(this)
  }

  handleChange(event) {
    console.log(event.target.value)
    this.props.onEmailChange(event.target.value);
  }

  handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
    this.props.onSubmitChange(true);
    // axios.post('http://localhost:5000/signup', {
    //   email: this.state.value
    // }).then(response => {
    //   console.log("VI HAR SENDT INN !!!:")
    // }).catch(err => console.log("Error"))

    axios.post('http://localhost:5000/signup',{'email':this.props.email})
    .then(response => {
      console.log(response)
      console.log("VI HAR SENDT INN !!!:")
      this.props.onAuthResponse(response);
      // this.setState({ trumfdata: response.data })
    })
    .catch(err => console.log("Error", err))
  }

  render() {
    return (
      <div>
      <img className="App-logo" src="lineup2Date.png"/>
      <br></br>
      <h3>Enter your Yahoo Fantasy Sports email to begin.</h3>
      <br></br>
      <form method="get" onSubmit={this.handleSubmit}>
        <label>
          Email:
          <input type="email" onChange={this.handleChange} />
        </label>
        <br></br>
        <input type="submit" value="Submit" />
      </form>
      </div>
    );
  }
}

export default Welcome;

// class Welcome extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = {email: ''};
//
//     this.handleChange = this.handleChange.bind(this);
//     this.handleSubmit = this.handleSubmit.bind(this);
//   }
//
//   handleChange(event) {
//     this.setState({email: event.target.value});
//   }
//
//   handleSubmit(event) {
//     // alert('A name was submitted: ' + this.state.value);
//     event.preventDefault();
//     console.log(this.state.email)
//     // axios.post('http://localhost:5000/signup', {
//     //   email: this.state.value
//     // }).then(response => {
//     //   console.log("VI HAR SENDT INN !!!:")
//     // }).catch(err => console.log("Error"))
//
//     axios.post('http://localhost:5000/signup',{'email':this.state.email})
//     .then(response => {
//       console.log("VI HAR SENDT INN !!!:")
//       // this.setState({ trumfdata: response.data })
//     })
//     .catch(err => console.log("Error", err))
//   }
//
//   render() {
//     return (
//       <div>
//       <h1>Welcome to LineUp2Date</h1>
//       <form method="get"onSubmit={this.handleSubmit}>
//         <label>
//           Email:
//           <input type="email" value={this.state.email} onChange={this.handleChange} />
//         </label>
//         <br></br>
//         <input type="submit" value="Submit" />
//       </form>
//       </div>
//     );
//   }
// }
//
// export default Welcome;
