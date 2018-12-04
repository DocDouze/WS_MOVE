
"use strict";

let SetTorqueLimit = require('./SetTorqueLimit.js')
let StopController = require('./StopController.js')
let SetSpeed = require('./SetSpeed.js')
let StartController = require('./StartController.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')
let RestartController = require('./RestartController.js')
let TorqueEnable = require('./TorqueEnable.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')

module.exports = {
  SetTorqueLimit: SetTorqueLimit,
  StopController: StopController,
  SetSpeed: SetSpeed,
  StartController: StartController,
  SetComplianceSlope: SetComplianceSlope,
  RestartController: RestartController,
  TorqueEnable: TorqueEnable,
  SetCompliancePunch: SetCompliancePunch,
  SetComplianceMargin: SetComplianceMargin,
};
