import { Component, OnInit } from '@angular/core';
import { trigger, state, style, transition, animate} from '@angular/animations';

@Component({
  selector: 'app-toppanel',
  templateUrl: './toppanel.component.html',
  styleUrls: ['./toppanel.component.css'],
  animations: [
    trigger('slideInOut', [
      state('out', style({
        transform: 'translate3d(0, 0, 0)'
      })), 
      state('in', style({
        transform: 'translate3d(0, -100%, 0)'
      })),
      transition('in => out', animate('500ms ease-in-out')),
      transition('out => in', animate('500ms ease-in-out'))
    ]),
  ]
})
export class ToppanelComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  menuState: string = "in";
  public visibility: string = "visible";

  toggleTopPanel() {
    this.menuState = this.menuState === 'out' ? 'in' : 'out';
  }

  toggleToggleVisibility() {
    this.visibility = this.visibility === 'visible' ? 'hidden' : 'visible';
  }
  setToggleVisibility(vis) {
    this.visibility = vis;
  }
}
