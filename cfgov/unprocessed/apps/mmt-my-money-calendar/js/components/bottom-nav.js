import clsx from 'clsx';
import { useCallback } from 'react';
import { observer } from 'mobx-react';
import { NavLink } from 'react-router-dom';
import { useStore } from '../stores';

import { calendar, add, idea, menu } from '../lib/icons';

const NavItem = ({ href, icon, label, badge, disabled = false, canSpotlight, ...params }) => {
  const classes = clsx('bottom-nav__link', disabled && 'disabled');
  const iconClasses = clsx('bottom-nav__link-icon');
  const labelClasses = clsx('bottom-nav__link-label');
  const addSpotlight = !localStorage.getItem('removeSpotlight') ? 'has-spotlight' : ''
  const clickHandler = useCallback(
    (event) => {
      if (!disabled) return true;

      event.preventDefault();
      event.stopPropagation();
    },
    [disabled]
  );

  return (
    <li className={`bottom-nav__item ${canSpotlight ? addSpotlight : ''}`}>
      <NavLink onClick={clickHandler} id="nav-link" className={classes} disabled={disabled} to={href} {...params}>
        <div className={iconClasses} dangerouslySetInnerHTML={{ __html: icon }} />
        <div className={labelClasses}>{label}</div>
        {!!badge && <div className="bottom-nav__link-badge">{badge}</div>}
      </NavLink>
    </li>
  );
};

function BottomNav() {
  const {
    uiStore,
    strategiesStore,
    eventStore: { hasStartingBalance },
  } = useStore();
  const classes = clsx('bottom-nav', uiStore.showBottomNav && 'bottom-nav--visible');

  if (!hasStartingBalance) return null;

  return (
    <footer className={classes}>
      <nav className="bottom-nav__nav">
        <ul className="bottom-nav__items">
          <NavItem href="/calendar" icon={calendar} exact label="Calendar" disabled={!hasStartingBalance} />
          <NavItem href="/calendar/add/income" icon={add} label="Income/Expense" disabled={!hasStartingBalance} />
          <NavItem
            href="/strategies"
            icon={idea}
            label="Strategies"
            badge={strategiesStore.strategyResults.length}
            disabled={!hasStartingBalance || !strategiesStore.strategyResults.length}
          />
          <NavItem href="/more" icon={menu} label="More" disabled={!hasStartingBalance} />
        </ul>
      </nav>
    </footer>
  );
}

export default observer(BottomNav);
