import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IopanelComponent } from './iopanel.component';

describe('IopanelComponent', () => {
  let component: IopanelComponent;
  let fixture: ComponentFixture<IopanelComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IopanelComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IopanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
