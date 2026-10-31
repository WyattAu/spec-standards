{
  description = "spec-standards devShell: prose gates, link checks, registry audits";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (s: f nixpkgs.legacyPackages.${s});
    in
    {
      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = with pkgs; [
            git
            gh
            lychee
            nodejs
            nodePackages.markdownlint-cli
            (python3.withPackages (ps: [ ps.pyyaml ]))
          ];
        };
      });
    };
}
