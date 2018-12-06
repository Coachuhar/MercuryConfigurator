import React, {Component} from 'react';

class Components extends Component{
    constructor(){
        super();
        this.state = {
            components: [],
        };
    }

    componentDidMount() {
        fetch('http://127.0.0.1:8000/api/components', {
            method: "GET",
        })
        .then(results => {
            return results.json();
       // }).then(data => {
         //   let components = data.results.map((item) => {
           //     return(
             //       <div key={item.results}>
               //     </div>
                //)
            //})
            //this.setState({components: components});
            
        })
    }

    render(){
        return (
            <div className="container2">
                    {this.state.components}
                </div>
        )
    }
}

export default Components;