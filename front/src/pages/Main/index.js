import React from 'react';
import {Link} from 'react-router-dom';

class Main extends React.Component {

    render() {
        return (
            <>
                
            <div>
                <h2>Aplicativo de Ajuda à Estudos</h2>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <ul className="navbar-nav mr-auto">
                        <li><Link to={'/continhas'} className="nav-link"> Aritmética &#215;&#247;</Link></li>
                        <li><Link to={'/continhasB'} className="nav-link"> Expressões Numéricas +-&#215; </Link></li>
                        <li><Link to={'/textos'} className="nav-link"> Qual é o animal? </Link></li>
                    </ul>
                </nav>
            </div>
            </>
        );
    }
}

export default Main;