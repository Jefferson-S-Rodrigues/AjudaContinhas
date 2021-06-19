import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Continhas from './pages/Continhas';
import ContinhasB from './pages/ContinhasB';
import Textos from './pages/Textos';
import Main from './pages/Main';

function Routes() {
    return (
        <Router>
            <Switch>
                <Route path="/" exact component={Main} />
                <Route path="/continhas" component={Continhas} />
                <Route path="/continhasB" component={ContinhasB} />
                <Route path="/textos" component={Textos} />
            </Switch>
        </Router>
    );
}

export default Routes;

/*

            <div>
                <h2>Aplicativo de Ajuda à Estudos</h2>
                <nav className="navbar navbar-expand-lg navbar-light bg-light">
                    <ul className="navbar-nav mr-auto">
                        <li><Link to={'/continhas'} className="nav-link"> Continhas </Link></li>
                        <li><Link to={'/continhasB'} className="nav-link"> Continhas Toinzin </Link></li>
                        <li><Link to={'/textos'} className="nav-link"> Textos Nina </Link></li>
                    </ul>
                </nav>
            </div>
*/