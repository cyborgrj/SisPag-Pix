DROP TABLE IF EXISTS pix CASCADE;

CREATE TABLE "pix" (
  "txtid" VARCHAR PRIMARY KEY UNIQUE,
  "name" VARCHAR NOT NULL,
  "valor" DECIMAL NOT NULL,
  "createdby" VARCHAR NOT NULL,
  "createdat" DATE NOT NULL,
  "status" VARCHAR NOT NULL,
  "updatedby" VARCHAR,
  "updatedat" DATE
);

